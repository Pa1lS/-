import sqlite3
import re


class Data_Base:
    CATEGOR = {0:"Rhythm",
                1: "Rhymes",
                2: "Wealth",
                3: "Images", 
                4: "Charisma",
                5: "Atmosphere"}
    def _check_parametrs(command):
        """Проверка команды на SQL-инъекцию"""
        # Паттерны, указывающие на возможные инъекции
        sql_patterns = [
            r"(\b(SELECT|INSERT|UPDATE|DELETE|WHERE|OR|AND|DROP|JOIN|EXEC|UNION|;|'|--|#|\\)\b)",
            r"(--|\bOR\b|\bAND\b|;|')"
        ]
        
        for pattern in sql_patterns:
            if re.search(pattern, command, re.IGNORECASE):
                return False
        return True
        
        
    
    def __command(self, command, param=None):
        """Функция проверяет команду на sql-инъекцию, и исполняет её, закрывая подключение к БД, если всё нормально, иначе, записывает в логи, что была введена не корректная команда"""
        if self._check_parametrs(command):
            try:
                conn = self.__create_connection(self.data_base)
                cursor = conn.cursor()
                if (param != None):
                    cursor.execute(command, param)
                else:
                    cursor.execute(command)
                    
                if command.strip().lower().startswith("select"):
                    results = cursor.fetchall()
                    self.__close(conn)
                    return results
                
                conn.commit()
                self.__close(conn)
                return True
            except sqlite3.Error as e:
                # Записать, что вышла ошибка, и вернуть False
                print(e)
                return False
        else:
            return f"<!> Не корректная сторока: {command}"

    
    def __create_connection(self, db_file): 
        return sqlite3.connect(db_file)


    def __close(self, conn):
        conn.close()
    
    
    def __create_db(self, conn):
        cursor = conn.cursor()
        cursor.execute('''
			CREATE TABLE IF NOT EXISTS artists (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
                photo TEXT NOT NULL
			)
		''')
        cursor.execute('''
			CREATE TABLE IF NOT EXISTS tracks (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				artist_id INTEGER NOT NULL,
				name TEXT,
				release_date TEXT,
                photo TEXT,
				FOREIGN KEY (artist_id) REFERENCES artists (id)
			)
		''')
        cursor.execute('''
			CREATE TABLE IF NOT EXISTS ratings (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				track_id INTEGER NOT NULL,
				Rhythm TEXT,
                Rhymes TEXT,
                Wealth TEXT,
                Images TEXT,
                Charisma TEXT,
                Atmosphere TEXT,
				FOREIGN KEY (track_id) REFERENCES tracks (id)
			)
		''')
        conn.commit()
        self.__close(conn)
        
        
    def __init__(self, data_base_file):
        self.data_base = data_base_file
        self.__create_db(self.__create_connection(self.data_base))
        
    
    def get_estimations(self, song_name): # <?> Возможно нужно будет удалить
        """Функция, которая возвращает всю нужную информацию об оценках, по названию трека"""
        """Возращается список. Первое число-сумма, второе число-кол-во оценок"""
        command = '''SELECT Rhythm, Rhymes, Wealth, Images, Charisma, Atmosphere FROM ratings 
                 INNER JOIN tracks ON ratings.track_id = tracks.id 
                 WHERE tracks.name = ?'''
        arr = self.__command(command=command, param=(song_name,))
        arr = arr[0]
        arr = [list(map(int, cat.split('.'))) for cat in arr]
        return arr

        
    def get_autor(self, name_autor= None, artist_id=None):
        """Функция, которая возвращает всю нужную информацию про автора"""
        if artist_id == None and name_autor != None:
            command =  '''SELECT name, photo FROM artists 
                    WHERE name = ?'''
            return self.__command(command=command, param=(name_autor,))
        elif artist_id != None and name_autor == None:
            command =  '''SELECT name, photo FROM artists 
                    WHERE id = ?'''
            return self.__command(command=command, param=(artist_id,))
        
        
    def get_song(self, song_name):
        """Функция, которая возвращает всю нужную информацию про трек"""
        command = """SELECT artist_id, name, release_date, photo FROM tracks WHERE name = ?"""
        result = self.__command(command=command, param=(song_name,))
        artist_name = self.get_autor(artist_id=result[0][0])
        return result[0][1:] + (artist_name,)
        
    
    def set_estimations_to_song(self, name_song:str, estimations:list):
        """Добавление оценок пользователя на трек"""
        old_estimations = self.get_estimations(name_song)
        for i in range(len(estimations)):
            old_estimations[i][0] += estimations[i]
            old_estimations[i][1] += 1
        a = tuple('.'.join(map(str, i)) for i in old_estimations)
        command = """UPDATE ratings 
                SET Rhythm = ?, 
                    Rhymes = ?, 
                    Wealth = ?, 
                    Images = ?, 
                    Charisma = ?, 
                    Atmosphere = ?, 
                    ocenka = ?
                INNER JOIN tracks ON ratings.track_id = tracks.id 
                WHERE tracks.name = ?"""
        self.__command(command=command, param=a + (name_song,))
        

    def _set_autor(self, name, path_to_photo):
        """Добавление нового автора"""
        command = """INSERT INTO artists(name, photo) VALUES(?, ?)"""
        self.__command(command=command, param=(name, path_to_photo))
    
    
    def _set_Song(self, artist_name, name, release_date):
        """Добавление нового трека"""
        artist_id = self.get_autor(artist_name)[0][1]
        command = """INSERT INTO tracks (artist_id, name, release_data) VALUES(?, ?, ?)"""
        self.__command(command=command, param=(artist_id, name, release_date))
        
    
    def _remove_Song(self, song_name):
        """Удаление трека из БД"""
        command = """DELET FROM tracks WHERE name = ?"""
        self.__command(command=command, param=(song_name,))
        


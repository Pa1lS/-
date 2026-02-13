package repository

import (
	"context"
	"danyazatvorchestvo/pkg/models"
)

func (repo *RepoDB) NewMusicDB(music models.Music) error {
	repo.mu.Lock()
	defer repo.mu.Unlock()
	_, err := repo.pool.Exec(context.Background(), ``, music.Name, music.AuthorID, music.GenreID, music.Slug)
	return err
}

func (repo *RepoDB) GetMusicDB(id int) (music models.Music, err error) {
	repo.mu.Lock()
	defer repo.mu.Unlock()
	err = repo.pool.QueryRow(context.Background(), ``, id).Scan(&music.Name, &music.AuthorID, &music.GenreID, &music.Slug)
	return music, err
}

func (repo *RepoDB) GetMusicsDB() (musics []models.Music, err error) {
	repo.mu.Lock()
	defer repo.mu.Unlock()
	rows, err := repo.pool.Query(context.Background(), ``)
	defer rows.Close()

	for rows.Next() {
		var music models.Music
		err = rows.Scan(
			&music.ID,
			&music.Name,
			&music.AuthorID,
			&music.GenreID,
			&music.Slug,
		)
		if err != nil {
			return nil, err
		}
		musics = append(musics, music)
	}
	return musics, nil
}

func (repo *RepoDB) UpdateMusicDB(id int, music models.Music) error {
	repo.mu.Lock()
	defer repo.mu.Unlock()
	_, err := repo.pool.Exec(context.Background(), ``, id, &music.Name, &music.AuthorID, &music.GenreID, &music.Slug)
	return err
}

func (repo *RepoDB) DeleteMusicDB(id int) error {
	repo.mu.Lock()
	defer repo.mu.Unlock()
	_, err := repo.pool.Exec(context.Background(), ``, id)
	return err
}

package repository

import "danyazatvorchestvo/pkg/models"

func (repo *RepoDB) NewUserDB(user models.User) error {
	repo.pool.Exec()
}

func (repo *RepoDB) GetUserDB(id int) (user models.User, err error) {

}

func (repo *RepoDB) GetUsersDB() (users []models.User, err error) {

}

func (repo *RepoDB) UpdateUserDB(id int, user models.User) error {

}

func (repo *RepoDB) DeleteUserDB(id int) error {

}

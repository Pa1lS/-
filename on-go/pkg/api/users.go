package api

import "net/http"

func (api *api) GetUser(w http.ResponseWriter, r *http.Request) { // для админов

}

func (api *api) NewUser(w http.ResponseWriter, r *http.Request) {

}

func (api *api) UpdateUser(w http.ResponseWriter, r *http.Request) { // для админов и самого пользователя
}

func (api *api) DeleteUser(w http.ResponseWriter, r *http.Request) { // для админов и самого пользователя

}

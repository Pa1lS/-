package api

import (
	"danyazatvorchestvo/pkg/repository"

	"github.com/gorilla/mux"
)

type api struct {
	r  *mux.Router
	db *repository.RepoDB
}

func New(router *mux.Router, db *repository.RepoDB) *api {
	return &api{r: router, db: db}
}

func (api *api) Handlers() {
	// api.r.HandleFunc()
}

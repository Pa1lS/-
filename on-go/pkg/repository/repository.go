package repository

import (
	"context"
	"sync"

	"github.com/jackc/pgx/v4/pgxpool"
)

type RepoDB struct {
	mu   sync.Mutex
	pool *pgxpool.Pool
}

func (repo *RepoDB) Close() error {
	// panic("unimplemented")
	return nil
}
func New(db_addr string) (*RepoDB, error) {
	pool, err := pgxpool.Connect(context.Background(), "") // данные вынести для защиты
	if err != nil {
		return nil, err
	}
	return &RepoDB{mu: sync.Mutex{}, pool: pool}, nil
}

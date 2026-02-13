package models

import "time"

type User struct {
	ID           uint32
	Name         string
	PassWordHash string
	CreateAt     time.Time
}

type Author struct {
	ID   int
	Name string
}

type Genre struct {
	ID   int
	Name string
}

type Music struct {
	ID         uint32
	Name       string
	AuthorID   int
	GenreID    int
	Slug       string
	KolvoScore uint32
	ScoreSum   uint32
}

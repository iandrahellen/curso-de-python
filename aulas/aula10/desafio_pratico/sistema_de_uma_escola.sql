create database if not exists escola;
use escola;

create table alunos(
 id int,
 nome varchar(50),
 idade int,
 endereco varchar(30)
);

create table professores(
 id_matricula int,
 nome varchar(30),
 especilialidade varchar(40),
 endereco varchar(30)
);

create table turmas(
 id int,
 hr_inicio int,
 hr_termino int,
 dia_semana varchar(20)
);

create table disciplinas(
 id int,
 nome_disc varchar(20),
 qtd_aulas int
);
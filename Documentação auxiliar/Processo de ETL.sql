-- Procedures e eventos do sistema dashboard académico

use mydb;
SET FOREIGN_KEY_CHECKS = 0;
SET SQL_SAFE_UPDATES = 0;

-- Insert dimensão aluno
delimiter //
CREATE PROCEDURE procAluno()
BEGIN
INSERT INTO mydb.Dim_aluno (idAluno_trans, nome_pessoa, matricula)
select a.id, concat('Aluno',a.id), a.matricula 
from eies.adm_pessoa p
inner join eies.wac_aluno a on p.id = a.pessoa_id;
END//


-- Insert dimensão professor
delimiter //
CREATE PROCEDURE procProfessor()
BEGIN
INSERT INTO mydb.Dim_professor (idProfessor_trans, nome_pessoa, matricula)
select prof.id, concat('Professor',cast(Lpad(prof.id,3,0)as char)), prof.matricula 
from eies.adm_pessoa p
inner join eies.wac_professor prof on p.id = prof.pessoa_id;
END//


-- Insert dimensão periodo
delimiter //
CREATE PROCEDURE procPeriodo()
BEGIN
INSERT INTO mydb.Dim_periodo (idPeriodo_trans, ano, semestre)
select per.ano, per.semestre
from eies.wac_periodo per;
END//


-- Insert dimensão turma de ingresso
delimiter //
CREATE PROCEDURE procTurmaIngresso()
BEGIN
INSERT INTO mydb.Dim_turmaDeIngresso (idturma_trans, descricao, turno)
select t.id, t.descricao, t.turno
from eies.wac_turmaingresso t;
END//


-- insert dimensão disciplina
delimiter //
CREATE PROCEDURE procDisciplina()
BEGIN
INSERT INTO mydb.Dim_disciplina (idDisciplina_trans, codigo_disciplina, nome)
select d.id, d.codigo_disciplina, d.nome
from eies.wac_disciplina d;
END//


-- dados avaliação
delimiter //
CREATE PROCEDURE procAvaliacao()
BEGIN
INSERT INTO mydb.Dim_avaliacao (idAvaliacao_trans, descricao)
select a.id, a.descricao
from eies.wac_avaliacao a;
END//


-- idados grupo avaliação
delimiter //
CREATE PROCEDURE procGrupoAvaliacao()
BEGIN
INSERT INTO mydb.Dim_grupoAvaliacao (descricao, idGrupoAvaliacao_trans)
select g.descricao, g.id
from eies.wac_grupoavaliacao g
where g.ativo = 1;
END//


-- daos pautas
delimiter //
CREATE PROCEDURE procPauta()
BEGIN
INSERT INTO mydb.Dim_pauta (idPauta_trans, identificador)
select p.id, p.identificador
from eies.wac_pauta p;
END//


-- dados fato desempenho
delimiter //
CREATE PROCEDURE procDesempenho()
BEGIN
INSERT INTO mydb.Fato_desempenhoAluno (Dim_aluno_idDim_aluno, Dim_grupoAvaliacao_idDim_grupoAvaliacao
, Dim_turmaDeIngresso_idDim_turmaDeIngresso, Dim_pauta_idDim_pauta, Dim_disciplina_idDim_disciplina, 
Dim_periodo_idDim_periodo, media)
select distinct dwa.idDim_aluno, dwg.idDim_grupoAvaliacao, dwt.idDim_turmaDeIngresso, dwp.idDim_pauta, 
dwd.idDim_disciplina, dwper.idDim_periodo, sum(av.nota)/count(wa.id)
from eies.wac_aluno wa
inner join eies.wac_nota n on wa.id = n.aluno_id
inner join eies.wac_avaliacao av on n.avaliacao_id = av.id
inner join eies.wac_grupoavaliacao ga on av.grupo_avaliacao_id = ga.id
inner join eies.wac_turmaingresso wt on wa.turma_ingresso_id = wt.id
inner join eies.wac_pauta wp on wap.pauta_id = wp.id
inner join eies.wac_periodo wper on wp.periodo_id = wper.id
inner join eies.wac_disciplina wd on wp.disciplina_id = wd.id
inner join mydb.Dim_aluno dwa on wa.id = dwa.idAluno_trans
inner join mydb.Dim_grupoAvaliacao dwg on ga.id = dwg.idGrupoAvaliacao_trans
inner join mydb.Dim_turmaDeIngresso dwt on wt.id = dwt.idturma_trans
inner join mydb.Dim_pauta dwp on wp.id = dwp.idPauta_trans
inner join mydb.Dim_disciplina dwd on wd.id = dwd.idDisciplina_trans
inner join mydb.Dim_periodo dwper on wper.id = dwper.idPeriodo_trans;
END//

-- dados fato absenteismo
delimiter //
CREATE PROCEDURE procAbsenteismo()
BEGIN
INSERT INTO mydb.Fato_absenteismo (Dim_frequencia_idDim_frequencia, Dim_aluno_idDim_aluno, Dim_grupoAvaliacao_idDim_grupoAvaliacao
, Dim_turmaDeIngresso_idDim_turmaDeIngresso, Dim_pauta_idDim_pauta, Dim_disciplina_idDim_disciplina, 
Dim_periodo_idDim_periodo, qtd_falta)
select distinct dwa.idDim_aluno, dwg.idDim_grupoAvaliacao, dwt.idDim_turmaDeIngresso, dwp.idDim_pauta, 
dwd.idDim_disciplina, dwper.idDim_periodo
from eies.wac_aluno wa
inner join eies.wac_nota n on wa.id = n.aluno_id
inner join eies.wac_avaliacao av on n.avaliacao_id = av.id
inner join eies.wac_grupoavaliacao ga on av.grupo_avaliacao_id = ga.id
inner join eies.wac_turmaingresso wt on wa.turma_ingresso_id = wt.id
inner join eies.wac_pauta wp on wap.pauta_id = wp.id
inner join eies.wac_periodo wper on wp.periodo_id = wper.id
inner join eies.wac_disciplina wd on wp.disciplina_id = wd.id
inner join mydb.Dim_aluno dwa on wa.id = dwa.idAluno_trans
inner join mydb.Dim_grupoAvaliacao dwg on ga.id = dwg.idGrupoAvaliacao_trans
inner join mydb.Dim_turmaDeIngresso dwt on wt.id = dwt.idturma_trans
inner join mydb.Dim_pauta dwp on wp.id = dwp.idPauta_trans
inner join mydb.Dim_disciplina dwd on wd.id = dwd.idDisciplina_trans
inner join mydb.Dim_periodo dwper on wper.id = dwper.idPeriodo_trans;
END//
 

CREATE EVENT evAluno
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 7 DAY
DO CALL procAluno;

CREATE EVENT evProfessor
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 7 DAY
DO CALL procProfessor;

CREATE EVENT evPeriodo
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 7 DAY
DO CALL procPeriodo;

CREATE EVENT evTurmaIngresso
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 7 DAY
DO CALL procTurmaIngresso;

CREATE EVENT evDisciplina
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 7 DAY
DO CALL procDisciplina;

CREATE EVENT evAvaliacao
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 7 DAY
DO CALL procAvaliacao;

CREATE EVENT evGrupoAvaliacao
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 7 DAY
DO CALL procGrupoAvaliacao;

CREATE EVENT evPauta
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 7 DAY
DO CALL procPauta;


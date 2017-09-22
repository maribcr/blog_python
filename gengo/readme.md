#O que é o GEngo?
Plataforma para automatização de infográficos a partir dos dados do SDE. No momentos estamos rodando apenas o Público dos estádios do Brasil.

- [x] Público dos estádios do Brasil
- [ ] Notas Armando Nogueira
- [ ] Estátisticas de Equipes
- [ ] Estátisticas de Jogadores
- [ ] Apitômetro

#Público dos campeonatos
Gera páginas de alguns campeonatos e de todas as equipes das Séries A, B e C do futebol nacional. O processo de atualização funciona rodando os seguintes códigos na pasta do gengo seguinte maneira:

- python manage.py atualiza [atualiza os jogos dos últimos 7 dias]
- python manage.py build [gera as páginas estáticas via Bakery]
- python manage.py publish --no-delete [públicas as páginas no S3 sem deletar os demais arquivos]

É possível atualizar todo o mês utlizando um opcional de atualização:

- python manage.py atualiza --mes


#Referências
https://www.djangoproject.com/
https://github.com/datadesk/django-bakery

#Install componentes no gengo
- pip3 install django_bakery==0.7.8
- pip3 install Django==1.9.5
- pip3 install numpy==1.12.1

#Créditos
DevGE (somente Carlos Lemos... por hora)
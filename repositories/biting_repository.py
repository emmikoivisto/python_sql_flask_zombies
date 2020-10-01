from db.run_sql import run_sql
from models.biting import Biting
from models.human import Human
from models.zombie import Zombie
import repositories.zombie_repository as zombie_repository
import repositories.human_repository as human_repository

# save
def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    biting.id = results[0]['id']
    # return biting

# select_all
def select_all(id):

# select

# delete

# delete_all

# update

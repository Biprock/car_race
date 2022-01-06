from ursina import *
import ursina
from ursina import entity
from ursina import texture
from ursina import collider

app=Ursina()
camera.orthographic=True
camera.fov =10

car=Entity(
    model='quad',
    texture='assets/car.png',
    collider='box',
    scale=(1,2),
    
    
)

road1=Entity(
    model='quad',
    texture='assets/road2.png',
    scale=15,
    z=1
)

road2=duplicate(road1,y=15)
pair=[road1,road2]

enemies=[]
import random
def newenemy():
    val=random.uniform(-2,2)
    new=duplicate(
        car,
        texture='assets\enemy',
        x=2*val,
        y=25,
        color=color.random_color(),
        rotation_z=
        0 

    )
    enemies.append(new)
    invoke(newenemy,delay=0.5)
    
newenemy()


def update():
    car.x -=held_keys['l']*5*time.dt
    car.x +=held_keys['r']*5*time.dt
    for road in pair:
        road.y-=6*time.dt
        if road.y<-15:
            road.y+=30
    for enemy in enemies:
        if enemy.x<0:
            enemy.y -=10*time.dt   
        else:
            enemy.y -=5*time.dt     

app.run()


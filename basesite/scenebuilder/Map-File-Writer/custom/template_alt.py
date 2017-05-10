from models.clients import Map,Scene,Object,Entity
from utils.scene_utils import SceneUtils

class MapDoc():
    new_map = Map('custom_1')
    new_map.scene_size = 3000
    new_map.cell_size = 100
    scene_utils = SceneUtils(new_map)


    new_map.obj_defs ={
        'scenery_tile':'objects/scenery/sceneryBlockTile.png',
        'scenery_block':'objects/scenery/sceneryBlock.png',
        'scenery_tree':'objects/scenery/sceneryBlockTree.png',
        'big_red':'animations/bigredrotate/bigRed090.png',
        'enemy':'animations/bigredrotate_evil/bigRed090_evil.png',
        'next_scene_portal':'animations/portal_green/portal_green0.png',
        'prev_scene_portal':'animations/portal_blue/portal_blue0.png',
        'big_red_animation_pack':'animations/bigredrotate',
        'enemy_animation_pack':'animations/bigredrotate_evil',
        'next_scene_portal_animation_pack':'animations/portal_green',
        'prev_scene_portal_animation_pack':'animations/portal_blue'
    }

    new_map.obj_codes = {
        '0':'scenery_block',
        '1':'scenery_tree',
        '*':'scenery_tile',
        'e':('enemy',('enemy_animation_pack',0)),
        'p':('big_red',('big_red_animation_pack',0)),
        'n':('next_scene_portal',('next_scene_portal_animation_pack',90)),
        'b':('prev_scene_portal',('prev_scene_portal_animation_pack',90))
    }

    # =====

    scene0 = Scene('test-scene1','winbackground.jpg',new_map.scene_size,new_map.scene_size)

    scene_grid = '''
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,p,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,0,0,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,0,0,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,0,0,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,0,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,0,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,1,-,-,1,-,-,-,-,1,e,-,-,-,-,-,e,1,-,-,-,e,-,1,-,-,1,-,-,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
'''

    scene_utils.things_setup_from_grid(scene0,scene_grid)

    # =====

    new_map.scenes.append(scene0)

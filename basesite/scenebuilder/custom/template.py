from ..scene_models.clients import Map,Scene,Object,Entity
from ..utils.scene_utils import SceneUtils

class MapDoc():
    new_map = Map('custom')
    new_map.scene_size = 3000
    new_map.cell_size = 100
    scene_utils = SceneUtils(new_map)

    new_map.obj_defs ={
        'scenery_block':'objects/scenery/sceneryBlockTile.png',
        'scenery_block_lr':'objects/scenery/sceneryBlockTileLR.png',
        'scenery_block_ur':'objects/scenery/sceneryBlockTileUR.png',
        'scenery_block_ll':'objects/scenery/sceneryBlockTileLL.png',
        'scenery_block_ul':'objects/scenery/sceneryBlockTileUL.png',
        'scenery_steel':'objects/scenery/sceneryBlockSteel.png',
        'scenery_steel_lr':'objects/scenery/sceneryBlockSteelLR.png',
        'scenery_steel_ur':'objects/scenery/sceneryBlockSteelUR.png',
        'scenery_steel_ll':'objects/scenery/sceneryBlockSteelLL.png',
        'scenery_steel_ul':'objects/scenery/sceneryBlockSteelUL.png',
        'scenery_grass':'objects/scenery/sceneryGrassTile.png',
        'scenery_grass_lr':'objects/scenery/sceneryGrassTileLR.png',
        'scenery_grass_ur':'objects/scenery/sceneryGrassTileUR.png',
        'scenery_grass_ll':'objects/scenery/sceneryGrassTileLL.png',
        'scenery_grass_ul':'objects/scenery/sceneryGrassTileUL.png',
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
        '0':'scenery_tree',
        '*':'scenery_block',
        '~':'scenery_block_lr',
        '^':'scenery_block_ur',
        '"':'scenery_block_ll',
        '`':'scenery_block_ul',
        '1':'scenery_steel',
        '2':'scenery_steel_lr',
        '3':'scenery_steel_ur',
        '4':'scenery_steel_ll',
        '5':'scenery_steel_ul',
        '#':'scenery_grass',
        '&':'scenery_grass_lr',
        '@':'scenery_grass_ur',
        '$':'scenery_grass_ll',
        '%':'scenery_grass_ul',
        'e':('enemy',('enemy_animation_pack',0)),
        'p':('big_red',('big_red_animation_pack',0)),
        'n':('next_scene_portal',('next_scene_portal_animation_pack',90)),
        'b':('prev_scene_portal',('prev_scene_portal_animation_pack',90))
    }

    # =====
#
    scene0 = Scene('test-scene1','maps/custom/dungeonBackground.jpg',new_map.scene_size,new_map.scene_size)
#
#     scene_grid0 = '''
# -,-,-,-,-,-,-,-,-,0,0,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,-,-,-,-,-,0,~,*,",0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,0,0,0,-,-,0,*,*,*,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,0,~,*,",0,-,0,*,p,*,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,0,*,e,*,0,-,0,*,*,*,",0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,0,^,*,`,0,-,0,*,*,*,*,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,0,0,0,-,-,0,*,*,*,`,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,-,-,-,-,-,0,*,*,*,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,-,-,-,-,-,0,*,*,*,0,-,-,-,-,0,0,0,-,-,-,-,-,-,-,-,-,-,
# -,-,-,-,-,-,-,0,~,*,*,*,",0,0,0,0,~,*,",0,0,0,0,0,0,0,0,0,-,
# -,-,-,-,-,-,0,~,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,",0,
# -,-,-,-,-,0,~,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,0,^,*,*,0,
# -,-,-,-,0,~,*,*,*,*,*,*,*,*,*,*,*,*,*,*,0,^,*,*,*,",0,*,`,0,
# -,-,-,0,~,*,*,*,*,*,*,*,`,0,0,^,*,*,*,*,",0,*,*,*,*,*,*,0,-,
# -,-,-,0,*,*,*,*,*,*,*,*,0,-,-,0,^,*,*,*,*,*,*,*,*,e,*,*,0,-,
# -,-,-,0,*,*,*,`,0,^,*,*,0,-,-,-,0,^,*,*,*,*,*,e,*,*,*,*,0,-,
# -,-,-,0,^,*,*,0,-,0,*,*,",0,-,-,-,0,^,*,*,*,*,*,*,e,*,*,",0,
# -,-,-,-,0,^,*,",0,~,*,*,*,0,-,-,-,-,0,*,*,*,*,*,*,*,*,n,*,0,
# -,-,-,-,-,0,^,*,*,*,e,*,`,0,-,-,-,-,0,*,*,*,*,*,*,*,*,*,`,0,
# -,-,-,-,-,-,0,*,*,*,*,`,0,-,-,-,-,0,~,*,*,`,0,0,0,0,0,0,0,-,
# -,-,-,-,-,-,0,*,*,*,`,0,-,-,-,-,0,~,*,*,`,0,-,-,-,-,-,-,-,-,
# -,-,-,-,-,-,0,*,*,*,0,-,-,-,-,0,~,*,*,`,0,-,-,-,-,-,-,-,-,-,
# -,-,-,-,-,-,0,*,*,*,0,-,-,-,0,~,*,*,`,0,-,-,-,-,-,-,-,-,-,-,
# -,-,-,-,-,-,0,*,*,*,",0,0,0,~,*,*,`,0,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,-,0,0,~,*,*,*,*,*,*,*,*,*,`,0,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,0,~,*,*,*,*,*,*,*,*,*,*,`,0,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,0,*,e,*,*,*,*,*,*,*,*,`,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,0,*,*,*,e,*,*,`,0,0,0,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,0,^,*,*,*,*,`,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# -,-,-,-,0,0,0,0,0,0,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,
# '''
#
#     scene_utils.things_setup_from_grid(scene0,scene_grid0)

    # =====

    # =====

    new_map.scenes.append(scene0)

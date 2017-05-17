from ..custom import template

def import_template() -> dict:
    line_buffer = []
    line_buffer.append(f'map custom')
    prefix = f'maps/custom'
    for scene in template.MapDoc.new_map.scenes:
        line_buffer.append(f'scene custom_scene')
        line_buffer.append(f'background {prefix}/{scene.background.path} {scene.background.size_x} {scene.background.size_y}')
        for entity in scene.entities:
            line_buffer.append('entity {}/{} {} {} {} {} {}/{} {} {}'.format(prefix,entity.path,entity.spawn_x,entity.spawn_y,entity.size_x,entity.size_y,prefix,entity.animation_path,entity.animation_rate,entity.does_clip))
        for thing in scene.objects:
            line_buffer.append('object {}/{} {} {} {} {} {}'.format(prefix,thing.path,thing.spawn_x,thing.spawn_y,thing.size_x,thing.size_y,thing.does_clip))

    line_buffer.append('\n')
    return line_buffer

def write_file(line_buffer,title):
    with open(f'{config.Java_Src_Dir}/{config.maps_dir}/{title}/{title}.map','w') as wtr:
        for line in line_buffer:
            wtr.write(f'{line}\n')

if __name__ == '__main__':
    map_buffer = import_template(template)
    write_file(map_buffer,template.MapDoc.new_map.source)
    source=template.MapDoc.new_map.source
    print(f'Generated map {config.Java_Src_Dir}/{config.maps_dir}/{source}/{source}.map\n')

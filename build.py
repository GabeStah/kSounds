import os

media_directory = os.getcwd() + '/media'
media_file_path = os.getcwd() + '/media.lua'

with open(media_file_path, 'w') as f:
    data = ['local LSM = LibStub("LibSharedMedia-3.0")\n']
    for file_name in os.listdir(media_directory):
        if (file_name.endswith('.ogg') or file_name.endswith('.mp3')):
            data.append('LSM:Register("sound", "|cFFAB0000%s|r", [[Interface\Addons\kSounds\media\%s]])\n' % (
                file_name, file_name))
    f.writelines(data)

#!/bin/zsh

photo_library_path="$HOME/Pictures/Photos.photoslibrary"
photo_originals="$photo_library_path/originals"
photo_processed="$HOME/Pictures/Handicraft1"

# atime The time file was last accessed
# date -r $(stat -f "%a" $FILE) +"%FT%T%z"
# mtime The time file was last modified
# date -r $(stat -f "%m" $FILE) +"%FT%T%z"
# ctime The time inode was last changed
# date -r $(stat -f "%c" $FILE) +"%FT%T%z"
# create time The time inode was created
# date -r $(stat -f "%B" $FILE) +"%FT%T%z"

read_dir(){
    #注意此处这是两个反引号，表示运行系统命令
    for file in `ls $1`
    do
        file_path="$1/$file"
        #注意此处之间一定要加上空格，否则会报错
        if [ -d $file_path ]; then
            read_dir $file_path
        else
            # echo $file_path
            if [[ $file =~ ".dng" ]]; then
                # echo $file >> "$HOME/Downloads/file_list_dng.txt"
                # date -r $(stat -f "%m" $file_path) +"%Y-%m-%d_%H.%M.%S" >> "$HOME/Downloads/file_list_dng.txt"
                modified_time=$(date -r $(stat -f "%m" $file_path) +"%Y-%m-%d_%H.%M.%S")
                mv "$file_path" "$photo_processed/$modified_time.dng"
            elif [[ $file =~ ".heic" ]] ;then
                # echo $file >> "$HOME/Downloads/file_list_heic.txt"
                modified_time=$(date -r $(stat -f "%m" $file_path) +"%Y-%m-%d_%H.%M.%S")
                mv "$file_path" "$photo_processed/$modified_time.heic"
            elif [[ $file =~ ".mov" ]] ;then
                # echo $file >> "$HOME/Downloads/file_list_mov.txt"
                modified_time=$(date -r $(stat -f "%m" $file_path) +"%Y-%m-%d_%H.%M.%S")
                mv "$file_path" "$photo_processed/$modified_time.mov"
            else
                # echo $file >> "$HOME/Downloads/file_list_other.txt"
                echo $file
            fi
        fi
    done
}

read_dir $photo_originals

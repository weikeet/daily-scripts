import os
import shutil

li_action = ['search', 'home', 'account_circle', 'settings', 'done', 'info', 'check_circle', 'delete', 'shopping_cart',
             'visibility', 'favorite', 'logout', 'description', 'favorite_border', 'lock', 'schedule', 'language',
             'face', 'help_outline', 'manage_accounts', 'fingerprint', 'filter_alt', 'event', 'verified', 'thumb_up',
             'dashboard', 'calendar_today', 'login', 'list', 'visibility_off', 'check_circle_outline', 'highlight_off',
             'date_range', 'help', 'question_answer', 'task_alt', 'paid', 'article', 'lightbulb', 'shopping_bag',
             'open_in_new', 'perm_identity', 'trending_up', 'credit_card', 'history', 'account_balance',
             'report_problem', 'delete_outline', 'fact_check', 'assignment', 'verified_user', 'arrow_right_alt',
             'star_rate', 'account_balance_wallet', 'autorenew', 'work', 'analytics', 'print', 'build', 'view_list',
             'today', 'store', 'delete_forever', 'admin_panel_settings', 'savings', 'room', 'lock_open', 'code',
             'grade', 'receipt', 'watch_later', 'update', 'add_shopping_cart', 'contact_support', 'power_settings_new',
             'pets', 'done_all', 'explore', 'bookmark', 'bookmark_border', 'reorder', 'note_add', 'account_box',
             'shopping_basket', 'pending_actions', 'payment', 'drag_indicator', 'launch', 'supervisor_account',
             'touch_app', 'zoom_in', 'pending', 'assessment', 'thumb_up_off_alt', 'done_outline', 'open_in_full',
             'leaderboard', 'exit_to_app', 'preview', 'assignment_ind']
li_audio_video = ['play_arrow', 'play_circle_filled', 'videocam', 'mic', 'play_circle', 'volume_up', 'pause',
                  'play_circle_outline', 'volume_off', 'replay', 'skip_next', 'library_books', 'speed', 'stop',
                  'fiber_manual_record', 'movie', 'skip_previous', 'new_releases', 'playlist_add', 'equalizer', 'loop',
                  'fast_forward', 'web', 'video_library', 'playlist_add_check', 'mic_off', 'library_add', 'video_call',
                  'pause_circle', 'subscriptions', 'repeat', 'shuffle', 'stop_circle', 'volume_mute', 'not_interested',
                  'mic_none', 'sort_by_alpha', 'library_music', 'fast_rewind', 'videocam_off', 'volume_down',
                  'queue_music', 'pause_circle_filled', 'recent_actors', 'web_asset', 'hearing', 'subtitles',
                  'library_add_check', 'album', 'fiber_new', 'pause_circle_outline', 'note', 'av_timer', 'radio',
                  'games', 'playlist_play', 'replay_circle_filled', 'branding_watermark', 'queue', 'forward_10',
                  'replay_10', 'closed_caption', 'video_settings', 'featured_play_list', 'control_camera', 'airplay',
                  'slow_motion_video', 'add_to_queue', 'playlist_add_check_circle', 'repeat_one', 'call_to_action',
                  'snooze', 'hd', 'high_quality', 'repeat_on', 'closed_caption_off', 'replay_30', 'featured_video',
                  '5g', 'shuffle_on', 'music_video', 'forward_30', 'replay_5', 'queue_play_next', 'art_track',
                  'playlist_remove', 'hearing_disabled', 'forward_5', 'playlist_add_circle', 'explicit', '4k',
                  'fiber_smart_record', 'video_label', 'closed_caption_disabled', 'remove_from_queue', 'repeat_one_on',
                  'surround_sound', 'interpreter_mode', 'web_asset_off', 'play_disabled']
li_device = ['light_mode', 'restart_alt', 'dark_mode', 'task', 'summarize', 'password', 'sell', 'signal_cellular_alt',
             'devices', 'settings_suggest', 'quiz', 'widgets', 'storage', 'battery_full', 'thermostat', 'credit_score',
             'gps_fixed', 'medication', 'price_check', 'pin', 'gpp_good', 'price_change', 'tungsten',
             'battery_charging_full', 'fmd_good', 'reviews', 'note_alt', 'air', 'graphic_eq', 'bluetooth', 'dvr',
             'nightlight', 'access_time', 'sports_score', 'water', 'share_location', 'gpp_maybe', 'monitor_heart',
             'cable', 'location_searching', 'cameraswitch', 'shortcut', 'airplane_ticket', 'device_thermostat',
             'monitor_weight', 'wallpaper', 'signal_wifi_4_bar', 'data_usage', 'radar', 'battery_std', 'gpp_bad',
             'developer_mode', 'bloodtype', 'wifi_tethering', 'mode_night', 'signal_cellular_4_bar', 'flashlight_on',
             'network_wifi', 'fmd_bad', 'splitscreen', 'airplanemode_active', 'access_time_filled', 'mobile_friendly',
             'battery_alert', 'sim_card_download', 'send_to_mobile', 'lens_blur', 'usb', 'signal_wifi_statusbar_4_bar',
             'screen_search_desktop', 'screen_rotation', 'signal_wifi_statusbar_connected_no_internet_4',
             'system_security_update_good', 'gps_not_fixed', 'bluetooth_connected', 'remember_me', 'pattern', 'nfc',
             'battery_saver', 'discount', 'brightness_high', 'mode_standby', 'storm', 'play_lesson', 'network_cell',
             'screenshot', 'data_saver_off', 'signal_wifi_0_bar', 'brightness_medium', 'brightness_low',
             'data_saver_on', 'bluetooth_searching', 'grid_4x4', 'ad_units', 'mobiledata_off', 'bluetooth_disabled',
             'security_update_good', 'signal_wifi_off', 'hdr_auto', 'battery_unknown']
li_image = ['edit', 'navigate_next', 'photo_camera', 'image', 'tune', 'picture_as_pdf', 'circle', 'receipt_long',
            'timer', 'auto_stories', 'collections', 'navigate_before', 'add_a_photo', 'auto_awesome', 'palette',
            'remove_red_eye', 'music_note', 'wb_sunny', 'add_photo_alternate', 'brush', 'flash_on', 'euro',
            'auto_fix_high', 'control_point', 'adjust', 'looks_one', 'style', 'camera', 'straighten', 'photo_library',
            'camera_alt', 'portrait', 'audiotrack', 'video_camera_front', 'rotate_right', 'grid_on', 'color_lens',
            'crop_free', 'landscape', 'timelapse', 'crop_square', 'slideshow', 'collections_bookmark', 'lens',
            'looks_two', 'panorama_fish_eye', 'filter_drama', 'filter_vintage', 'auto_awesome_motion', 'compare',
            'healing', 'image_search', 'rotate_left', 'crop', 'wb_incandescent', 'looks_3', 'blur_on',
            'center_focus_strong', 'currency_rupee', 'wb_cloudy', 'flare', 'face_retouching_natural', 'brightness_4',
            'colorize', 'filter_none', 'auto_awesome_mosaic', 'dehaze', 'assistant', 'cases', 'broken_image',
            'filter_center_focus', 'nature_people', 'photo', 'crop_original', 'flash_off', 'brightness_6', 'tag_faces',
            'brightness_5', 'details', 'grain', 'flip_camera_android', 'flip', 'loupe', 'brightness_1',
            'flip_camera_ios', 'movie_creation', 'image_not_supported', 'filter_1', 'panorama', 'add_to_photos',
            'auto_fix_normal', 'center_focus_weak', 'animation', 'movie_filter', 'looks_4', 'view_comfy', 'crop_din',
            'filter', 'control_point_duplicate', 'leak_add']
li_maps = ['local_shipping', 'place', 'menu_book', 'local_offer', 'map', 'badge', 'category', 'restaurant',
           'directions_car', 'volunteer_activism', 'local_fire_department', 'my_location', 'local_mall', 'flight',
           'near_me', 'handyman', 'directions_run', 'restaurant_menu', 'layers', 'medical_services', 'lunch_dining',
           'park', 'local_hospital', 'directions_walk', 'celebration', 'pin_drop', 'local_library', 'local_atm',
           'local_activity', 'local_cafe', 'delivery_dining', 'rate_review', 'person_pin', 'design_services',
           'directions_bike', 'fastfood', 'directions_bus', 'local_police', 'directions_car_filled', 'local_phone',
           'home_repair_service', 'zoom_out_map', 'local_grocery_store', 'miscellaneous_services', 'hotel',
           'cleaning_services', 'person_pin_circle', 'navigation', 'local_gas_station', 'local_florist', 'directions',
           'local_parking', 'train', 'money', 'local_post_office', 'two_wheeler', 'electrical_services', 'traffic',
           'alt_route', 'local_bar', 'pedal_bike', 'directions_boat', 'agriculture', 'add_business', '360', 'liquor',
           'beenhere', 'diamond', 'moving', 'local_airport', 'add_location_alt', 'maps_ugc', 'sailing', 'local_dining',
           'route', 'ramen_dining', 'local_taxi', 'hail', 'local_drink', 'local_pizza', 'local_printshop',
           'theater_comedy', 'trip_origin', 'local_laundry_service', 'not_listed_location', 'add_location',
           'dinner_dining', 'bakery_dining', 'directions_bus_filled', 'transfer_within_a_station', 'wine_bar',
           'multiple_stop', 'terrain', 'takeout_dining', 'emergency', 'icecream', 'local_pharmacy',
           'store_mall_directory', 'museum', 'factory']


def cpf(root_name, file_name, target_name):
    # print(target_name)
    if "action" in target_name:
        for filter_name in li_action:
            if filter_name in target_name:
                shutil.copyfile(root_name + '/' + file_name, target_name)
    elif "av" in target_name:
        for filter_name in li_audio_video:
            if filter_name in target_name:
                shutil.copyfile(root_name + '/' + file_name, target_name)
    elif "device" in target_name:
        for filter_name in li_device:
            if filter_name in target_name:
                shutil.copyfile(root_name + '/' + file_name, target_name)
    elif "image" in target_name:
        for filter_name in li_image:
            if filter_name in target_name:
                shutil.copyfile(root_name + '/' + file_name, target_name)
    elif "maps" in target_name:
        for filter_name in li_maps:
            if filter_name in target_name:
                shutil.copyfile(root_name + '/' + file_name, target_name)
    else:
        shutil.copyfile(root_name + '/' + file_name, target_name)


def findAllFile(base):
    i = 0
    for root, ds, fs in os.walk(base):
        for f in fs:
            # yield f
            root_name = str(root)
            file_name = str(f)
            if root_name.endswith("drawable") and file_name.endswith("24.xml"):
                # print(root, f)
                i = i + 1
                root_names = root_name.split('/')
                target_name = "/Users/weiwei/Pictures/AwesomeIcons/mdIcons/md_ic_" + root_names[6] + "_"
                if file_name.startswith("baseline_"):
                    target_name = target_name + file_name.replace("baseline_", "").replace("24.xml", "") + "baseline.xml"
                    cpf(root_name, file_name, target_name)
                elif file_name.startswith("outline_"):
                    target_name = target_name + file_name.replace("outline_", "").replace("24.xml", "") + "outline.xml"
                    cpf(root_name, file_name, target_name)
                elif file_name.startswith("round_"):
                    target_name = target_name + file_name.replace("round_", "").replace("24.xml", "") + "round.xml"
                    cpf(root_name, file_name, target_name)
                elif file_name.startswith("sharp_"):
                    target_name = target_name + file_name.replace("sharp_", "").replace("24.xml", "") + "sharp.xml"
                    cpf(root_name, file_name, target_name)
                elif file_name.startswith("twotone_"):
                    target_name = target_name + file_name.replace("twotone_", "").replace("24.xml", "") + "twotone.xml"
                    cpf(root_name, file_name, target_name)
    print(i)


def main():
    base = '/Users/weiwei/Pictures/AwesomeIcons/android'
    findAllFile(base)
    # for i in findAllFile(base):
    #     print(i)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.abspath(__file__).split('demos')[0])

from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.utils import get_hex_from_color

from screens import Screens

from kivymd.utils.cropimage import crop_image
from kivymd.fanscreenmanager import MDFanScreen
from kivymd.popupscreen import MDPopupScreen
from kivymd.button import MDIconButton
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
from kivymd.material_resources import DEVICE_TYPE
from kivymd.selectioncontrols import MDCheckbox
from kivymd.theming import ThemeManager
from kivymd.ripplebehavior import CircularRippleBehavior
from kivymd.cards import MDCard
from kivymd.list import OneLineListItem
from kivymd.icon_definitions import md_icons


def toast(text):
    # FIXME: crush with Python3.
    try:
        from kivymd.toast import toast
    except TypeError:
        from kivymd.toast.kivytoast import toast
    toast(text)


main_widget_kv = '''
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import images_path kivymd.images_path
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import MDLabel kivymd.label.MDLabel
#:import MDDropdownMenu kivymd.menus.MDDropdownMenu


<ContentPopup@BoxLayout>
    orientation: 'vertical'
    padding: dp(1)
    spacing: dp(30)

    Image:
        id: image
        source: 'assets/guitar-1139397_1280_crop.png'
        size_hint: 1, None
        height: dp(Window.height * 35 // 100)
        allow_stretch: True
        keep_ratio: False

    MDRoundFlatButton:
        text: 'Open Menu'
        pos_hint: {'center_x': .5}
        on_release: root.parent.show()

    Widget:


<ContentForAnimCard>
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        Widget:

        MDRoundFlatButton:
            text: "Free call"
            on_press: root.callback(self.text)

        Widget:

        MDRoundFlatButton:
            text: "Free message"
            on_press: root.callback(self.text)

        Widget:

    OneLineIconListItem:
        text: "Video call"
        on_press: root.callback(self.text)

        IconLeftSampleWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]"\
            % get_hex_from_color(app.theme_cls.primary_color)
        # FIXME: Don't work "secondary_text_color" parameter
        # secondary_text_color: app.theme_cls.primary_color

        IconLeftSampleWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]"\
            % get_hex_from_color(app.theme_cls.primary_color)

        IconLeftSampleWidget:
            icon: 'remote'


<MyNavigationDrawerIconButton@NavigationDrawerIconButton>
    icon: 'checkbox-blank-circle'


<ContentNavigationDrawer@MDNavigationDrawer>
    drawer_logo: './assets/drawer_logo.png'
    use_logo: 'logo'

    NavigationDrawerSubheader:
        text: "Menu of Examples:"

    MyNavigationDrawerIconButton:
        text: "Accordion"
        on_release:
            app.show_accordion()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Bottom App Bar"
        on_release:
            app.show_app_bar()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Accordion List"
        on_release:
            app.show_accordion_list()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Bottom Navigation"
        on_release:
            app.show_bottom_navigation()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Bottom Sheets"
        on_release:
            app.show_bottom_sheet()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Buttons"
        on_release:
            app.show_buttons()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Cards"
        on_release:
            app.show_cards()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Chips"
        on_release:
            app.show_chips()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Dialogs"
        on_release: 
            app.show_dialogs()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Download File"
        on_release:
            app.show_download_file()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Files Manager"
        on_release:
            app.show_file_manager()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Fan Manager"
        on_release:
            app.show_fan_manager()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Grid lists"
        on_release:
            app.show_grid()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Labels"
        on_release:
            app.show_labels()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Lists"
        on_release:
            app.show_lists()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "MD Icons"
        on_release:
            app.show_md_icons(app)
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Menus"
        on_release:
            app.show_menu()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Pickers"
        on_release:
            app.show_pickers()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Progress & activity"
        on_release:
            app.show_progress()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Popup Screen"
        on_release:
            app.show_popup_screen()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Progress bars"
        on_release:
            app.show_progress_bar()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Selection controls"
        on_release:
            app.show_selection_controls()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Sliders"
        on_release:
            app.show_sliders()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Stack Floating Buttons"
        on_release:
            app.show_stack_buttons()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Snackbars"
        on_release:
            app.show_snackbar()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Tabs"
        on_release:
            app.show_tabs()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Manager Swiper"
        on_release:
            app.show_manager_swiper()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Text fields"
        on_release:
            app.show_textfields()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Themes"
        on_release:
            app.show_theming()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "MDToolbars"
        on_release:
            app.show_toolbars()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "Update Screen Widget"
        on_release:
            app.show_update_spinner()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "User Animation Card"
        on_release:
            app.show_user_animation_card()
            app.set_title_toolbar(self.text)

NavigationLayout:
    id: nav_layout

    ContentNavigationDrawer:
        id: nav_drawer

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: toolbar
            title: app.title
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            elevation: 10
            left_action_items:
                [['menu', lambda x: app.root.toggle_nav_drawer()]]
            right_action_items:
                [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]

        ScreenManager:
            id: scr_mngr

            Screen:
                name: 'previous'

                FloatLayout:

                    Image:
                        source: '{}kivymd_logo.png'.format(images_path)
                        opacity: .3

                    BoxLayout:
                        orientation: 'vertical'
                        spacing: dp(10)
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': .5, 'center_y': .5}

                        MDLabel:
                            text: app.previous_text
                            size_hint_y: None
                            height: self.texture_size[1]
                            font_style: 'Subtitle1'
                            theme_text_color: 'Primary'
                            markup: True
                            halign: 'center'
                            text_size: self.width - 20, None

                        MDRaisedButton:
                            text: 'Click Me'
                            pos_hint: {'center_x': .5}
                            on_release:
                                app.show_shop_window()
                                app.instance_menu_demo_apps = MDDropdownMenu(items=app.menu_for_demo_apps, max_height=dp(260), width_mult=4)
                                app.instance_menu_demo_apps.open(self)

                        MDLabel:
                            text: app.previous_text_end
                            size_hint_y: None
                            height: self.texture_size[1]
                            font_style: 'Subtitle1'
                            theme_text_color: 'Primary'
                            markup: True
                            halign: 'center'
                            text_size: self.width - 20, None
'''


class KitchenSink(App, Screens):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    previous_date = ObjectProperty()
    title = "Kitchen Sink"
    # theme_cls.theme_style = 'Dark'

    def __init__(self, **kwargs):
        super(KitchenSink, self).__init__(**kwargs)

        self.menu_items = [
            {'viewclass': 'MDMenuItem',
             'text': 'Example item %d' % i,
             'callback': self.callback_for_menu_items}
            for i in range(15)
        ]
        self.Window = Window
        self.manager = None
        self.md_app_bar = None
        self.instance_menu_demo_apps = None
        self.md_theme_picker = None
        self.long_dialog = None
        self.input_dialog = None
        self.alert_dialog = None
        self.ok_cancel_dialog = None
        self.long_dialog = None
        self.dialog = None
        self.manager_open = False
        self.cards_created = False
        self.user_card = None
        self.bs_menu_1 = None
        self.bs_menu_2 = None
        self.my_snackbar = None
        self._interval = 0
        self.tick = 0
        self.create_stack_floating_buttons = False
        self.previous_text = \
            "Welcome to the application [b][color={COLOR}]Kitchen Sink"\
            "[/color][/b].\nTo see [b][color={COLOR}]KivyMD[/color][/b] "\
            "examples, open the menu and select from the list the desired "\
            "example or".format(COLOR=get_hex_from_color(
                self.theme_cls.primary_color))
        self.previous_text_end = \
            "for show example apps\n\n"\
            "Author - [b][color={COLOR}]Andrés Rodríguez[/color][/b]\n"\
            "[u][b][color={COLOR}]andres.rodriguez@lithersoft.com[/color]"\
            "[/b][/u]\n\n"\
            "Author this Fork - [b][color={COLOR}]Ivanov Yuri[/color][/b]\n"\
            "[u][b][color={COLOR}]kivydevelopment@gmail.com[/color]"\
            "[/b][u]".format(COLOR=get_hex_from_color(
                self.theme_cls.primary_color))
        self.names_contacts = (
            'Alexandr Taylor', 'Yuri Ivanov', 'Robert Patric', 'Bob Marley',
            'Magnus Carlsen', 'Jon Romero', 'Anna Bell', 'Maxim Kramerer',
            'Sasha Gray', 'Vladimir Ivanenko'
        )
        self.demo_apps_list = ['Shop Window']
        self.menu_for_demo_apps = []
        Window.bind(on_keyboard=self.events)
        crop_image((Window.width, int(dp(Window.height * 35 // 100))),
                   '{}/assets/guitar-1139397_1280.png'.format(
                       self.directory),
                   '{}/assets/guitar-1139397_1280_crop.png'.format(
                       self.directory))

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        if not os.path.exists(
                os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image

    def theme_picker_open(self):
        if not self.md_theme_picker:
            from kivymd.pickers import MDThemePicker
            self.md_theme_picker = MDThemePicker()
        self.md_theme_picker.open()

    def example_add_stack_floating_buttons(self):
        from kivymd.stackfloatingbuttons import MDStackFloatingButtons

        def set_my_language(instance_button):
            toast(instance_button.icon)

        if not self.create_stack_floating_buttons:
            screen = self.main_widget.ids.scr_mngr.get_screen('stack buttons')
            screen.add_widget(MDStackFloatingButtons(
                icon='lead-pencil',
                floating_data={
                    'Python': 'language-python',
                    'Php': 'language-php',
                    'C++': 'language-cpp'},
                callback=set_my_language))
            self.create_stack_floating_buttons = True

    def set_accordion_list(self):
        from kivymd.accordionlistitem import MDAccordionListItem

        def callback(text):
            toast('{} to {}'.format(text, content.name_item))

        content = ContentForAnimCard(callback=callback)

        for name_contact in self.names_contacts:
            self.accordion_list.ids.anim_list.add_widget(
                MDAccordionListItem(content=content,
                                    icon='assets/kivymd_logo.png',
                                    title=name_contact))

    def set_chevron_back_screen(self):
        """Sets the return chevron to the previous screen in ToolBar."""

        self.main_widget.ids.toolbar.right_action_items = [
            ['dots-vertical', lambda x: self.root.toggle_nav_drawer()]]

    def download_progress_hide(self, instance_progress, value):
        """Hides progress progress."""

        self.main_widget.ids.toolbar.right_action_items =\
            [['download',
              lambda x: self.download_progress_show(instance_progress)]]

    def download_progress_show(self, instance_progress):
        self.set_chevron_back_screen()
        instance_progress.open()
        instance_progress.animation_progress_from_fade()

    def show_example_download_file(self, interval):
        from kivymd.progressloader import MDProgressLoader

        def get_connect(host="8.8.8.8", port=53, timeout=3):
            import socket
            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                    (host, port))
                return True
            except (TimeoutError, ConnectionError, OSError):
                return False

        if get_connect():
            link = 'https://www.python.org/ftp/python/3.5.1/'\
                   'python-3.5.1-embed-win32.zip'
            progress = MDProgressLoader(
                url_on_image=link,
                path_to_file=os.path.join(self.directory, 'python-3.5.1.zip'),
                download_complete=self.download_complete,
                download_hide=self.download_progress_hide
            )
            progress.start(self.download_file.ids.box_flt)
        else:
            toast('Connect error!')

    def download_complete(self):
        self.set_chevron_back_screen()
        toast('Done')

    def file_manager_open(self):
        from kivymd.filemanager import MDFileManager
        from kivymd.dialog import MDDialog

        def open_file_manager(text_item, dialog):
            previous = False if text_item == 'List' else True
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(exit_manager=self.exit_manager,
                                              select_path=self.select_path,
                                              previous=previous)
            self.manager.add_widget(self.file_manager)
            self.file_manager.show(self.user_data_dir)
            self.manager_open = True
            self.manager.open()

        MDDialog(
            title='Title', size_hint=(.8, .4), text_button_ok='List',
            text="Open manager with 'list' or 'previous' mode?",
            text_button_cancel='Previous',
            events_callback=open_file_manager).open()

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.
        :type path: str;
        :param path: path to the selected directory or file;
        """

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager.dismiss()
        self.manager_open = False
        self.set_chevron_menu()

    def set_chevron_menu(self):
        self.main_widget.ids.toolbar.left_action_items = [
            ['menu', lambda x: self.root.toggle_nav_drawer()]]

    def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device.."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def add_cards(self, instance_grid_card):
        from kivymd.cards import MDCardPost

        def callback(instance, value):
            if value is None:
                toast('Delete post %s' % str(instance))
            elif isinstance(value, int):
                toast('Set like in %d stars' % value)
            elif isinstance(value, str):
                toast('Repost with %s ' % value)
            elif isinstance(value, list):
                toast(value[1])

        if not self.cards_created:
            self.cards_created = True
            menu_items = [
                {'viewclass': 'MDMenuItem',
                 'text': 'Example item %d' % i,
                 'callback': self.callback_for_menu_items}
                for i in range(2)
            ]
            buttons = ['facebook', 'vk', 'twitter']

            instance_grid_card.add_widget(
                MDCardPost(text_post='Card with text',
                           swipe=True, callback=callback))
            instance_grid_card.add_widget(
                MDCardPost(
                    right_menu=menu_items, swipe=True,
                    text_post='Card with a button to open the menu MDDropDown',
                    callback=callback))
            instance_grid_card.add_widget(
                MDCardPost(
                    likes_stars=True, callback=callback, swipe=True,
                    text_post='Card with asterisks for voting.'))

            instance_grid_card.add_widget(
                MDCardPost(
                    source="./assets/kitten-1049129_1280.png",
                    tile_text="Little Baby",
                    tile_font_style="H5",
                    text_post="This is my favorite cat. He's only six months "
                              "old. He loves milk and steals sausages :) "
                              "And he likes to play in the garden.",
                    with_image=True, swipe=True, callback=callback,
                    buttons=buttons))

    def update_screen(self, instance):
        def update_screen(interval):
            self.tick += 1
            if self.tick > 2:
                instance.update = True
                self.tick = 0
                self.update_spinner.ids.upd_lbl.text = "New string"
                Clock.unschedule(update_screen)

        Clock.schedule_interval(update_screen, 1)

    main_widget = None

    def build(self):
        self.main_widget = Builder.load_string(main_widget_kv)
        # self.bottom_navigation_remove_mobile(self.main_widget)
        return self.main_widget

    def set_popup_screen(self, content_popup):
        popup_menu = ContentForAnimCard()
        popup_menu.add_widget(Widget(size_hint_y=None, height=dp(150)))
        popup_screen = self.popup_screen.ids.popup_screen
        popup_screen.screen = popup_menu
        popup_screen.background_color = [.3, .3, .3, 1]
        popup_screen.max_height = content_popup.ids.image.height + dp(5)

    def bottom_navigation_remove_mobile(self, widget):
        # Removes some items from bottom-navigation demo when on mobile
        if DEVICE_TYPE == 'mobile':
            widget.ids.bottom_navigation_demo.remove_widget(
                widget.ids.bottom_navigation_desktop_2)
        if DEVICE_TYPE == 'mobile' or DEVICE_TYPE == 'tablet':
            widget.ids.bottom_navigation_demo.remove_widget(
                widget.ids.bottom_navigation_desktop_1)

    def show_user_example_animation_card(self):
        from kivymd.useranimationcard import MDUserAnimationCard

        def main_back_callback():
            toast('Close card')

        if not self.user_card:
            self.user_card = MDUserAnimationCard(
                user_name="Lion Lion",
                path_to_avatar="./assets/guitar-1139397_1280.png",
                callback=main_back_callback)
            self.user_card.box_content.add_widget(
                ContentForAnimCard())
        self.user_card.open()

    def show_example_snackbar(self, snack_type):
        def callback(instance):
            toast(instance.text)

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.my_snackbar.duration:
                anim = Animation(y=dp(10), d=.2)
                anim.start(self.snackbar.ids.button)
                Clock.unschedule(wait_interval)
                self._interval = 0
                self.my_snackbar = None

        from kivymd.snackbars import Snackbar

        if snack_type == 'simple':
            Snackbar(text="This is a snackbar!").show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!",
                     button_callback=callback).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very "
                          "long snackbar!").show()
        elif snack_type == 'float':
            if not self.my_snackbar:
                self.my_snackbar = Snackbar(
                    text="This is a snackbar!", button_text='Button',
                    duration=3, button_callback=callback)
                self.my_snackbar.show()
                anim = Animation(y=dp(72), d=.2)
                anim.bind(on_complete=lambda *args: Clock.schedule_interval(
                    wait_interval, 0))
                anim.start(self.snackbar.ids.button)

    def show_example_input_dialog(self):
        def result(text_button, instance):
            toast(instance.text_field.text)

        if not self.input_dialog:
            from kivymd.dialog import MDInputDialog

            self.input_dialog = MDInputDialog(
                title='Title', hint_text='Hint text', size_hint=(.8, .4),
                text_button_ok='Ok', events_callback=result)
        self.input_dialog.open()

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            from kivymd.dialog import MDDialog

            self.alert_dialog = MDDialog(
                title='Title', size_hint=(.8, .4), text_button_ok='Ok',
                text="This is Alert dialog",
                events_callback=self.callback_for_menu_items)
        self.alert_dialog.open()

    def show_example_ok_cancel_dialog(self):
        if not self.ok_cancel_dialog:
            from kivymd.dialog import MDDialog

            self.ok_cancel_dialog = MDDialog(
                title='Title', size_hint=(.8, .4), text_button_ok='Ok',
                text="This is Ok Cancel dialog", text_button_cancel='Cancel',
                events_callback=self.callback_for_menu_items)
        self.ok_cancel_dialog.open()

    def show_example_long_dialog(self):
        if not self.long_dialog:
            from kivymd.dialog import MDDialog

            self.long_dialog = MDDialog(
                text="Lorem ipsum dolor sit amet, consectetur adipiscing "
                     "elit, sed do eiusmod tempor incididunt ut labore et "
                     "dolore magna aliqua. Ut enim ad minim veniam, quis "
                     "nostrud exercitation ullamco laboris nisi ut aliquip "
                     "ex ea commodo consequat. Duis aute irure dolor in "
                     "reprehenderit in voluptate velit esse cillum dolore eu "
                     "fugiat nulla pariatur. Excepteur sint occaecat "
                     "cupidatat non proident, sunt in culpa qui officia "
                     "deserunt mollit anim id est laborum.",
                title='Title', size_hint=(.8, .4), text_button_ok='Yes',
                events_callback=self.callback_for_menu_items)
        self.long_dialog.open()

    def get_time_picker_date(self, instance, time):
        """Get date for MDTimePicker from the screen Pickers."""

        self.pickers.ids.time_picker_label.text = str(time)
        self.previous_time = time

    def show_example_time_picker(self):
        """Show MDTimePicker from the screen Pickers."""

        from kivymd.pickers import MDTimePicker

        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time_picker_date)

        if self.pickers.ids.time_picker_use_previous_time.active:
            try:
                time_dialog.set_time(self.previous_time)
            except AttributeError:
                pass
        time_dialog.open()

    def set_previous_date(self, date_obj):
        """Set previous date for MDDatePicker from the screen Pickers."""

        self.previous_date = date_obj
        self.pickers.ids.date_picker_label.text = str(date_obj)

    def show_example_date_picker(self):
        """Show MDDatePicker from the screen Pickers."""

        from kivymd.pickers import MDDatePicker

        if self.pickers.ids.date_picker_use_previous_date.active:
            pd = self.previous_date
            try:
                MDDatePicker(self.set_previous_date,
                             pd.year, pd.month, pd.day).open()
            except AttributeError:
                MDDatePicker(self.set_previous_date).open()
        else:
            MDDatePicker(self.set_previous_date).open()

    def show_example_bottom_sheet(self):
        """Show menu from the screen BottomSheet."""

        from kivymd.bottomsheet import MDListBottomSheet

        if not self.bs_menu_1:
            self.bs_menu_1 = MDListBottomSheet()
            self.bs_menu_1.add_item(
                "Here's an item with text only",
                lambda x: self.callback_for_menu_items(
                    "Here's an item with text only"))
            self.bs_menu_1.add_item(
                "Here's an item with an icon",
                lambda x: self.callback_for_menu_items(
                    "Here's an item with an icon"),
                icon='clipboard-account')
            self.bs_menu_1.add_item(
                "Here's another!",
                lambda x: self.callback_for_menu_items(
                    "Here's another!"),
                icon='nfc')
        self.bs_menu_1.open()

    def show_example_grid_bottom_sheet(self):
        """Show menu from the screen BottomSheet."""

        if not self.bs_menu_2:
            from kivymd.bottomsheet import MDGridBottomSheet

            self.bs_menu_2 = MDGridBottomSheet()
            self.bs_menu_2.add_item(
                "Facebook",
                lambda x: self.callback_for_menu_items("Facebook"),
                icon_src='./assets/facebook-box.png')
            self.bs_menu_2.add_item(
                "YouTube",
                lambda x: self.callback_for_menu_items("YouTube"),
                icon_src='./assets/youtube-play.png')
            self.bs_menu_2.add_item(
                "Twitter",
                lambda x: self.callback_for_menu_items("Twitter"),
                icon_src='./assets/twitter.png')
            self.bs_menu_2.add_item(
                "Da Cloud",
                lambda x: self.callback_for_menu_items("Da Cloud"),
                icon_src='./assets/cloud-upload.png')
            self.bs_menu_2.add_item(
                "Camera",
                lambda x: self.callback_for_menu_items("Camera"),
                icon_src='./assets/camera.png')
        self.bs_menu_2.open()

    def set_title_toolbar(self, title):
        """Set string title in MDToolbar for the whole application."""

        self.main_widget.ids.toolbar.title = title

    def set_appbar(self):
        """Create MDBottomAppBar for the screen BottomAppBar."""

        from kivymd.toolbar import MDBottomAppBar

        def press_button(inctance):
            toast('Press Button')

        self.md_app_bar = MDBottomAppBar(
            md_bg_color=self.theme_cls.primary_color,
            left_action_items=[
                ['menu', lambda x: x],
                ['clock', lambda x: x],
                ['dots-vertical', lambda x: x]],
            anchor='right', callback=press_button)

    def move_item_menu(self, anchor):
        """Sets icons in MDBottomAppBar for the screen BottomAppBar."""

        md_app_bar = self.md_app_bar
        if md_app_bar.anchor != anchor:
            if len(md_app_bar.right_action_items):
                md_app_bar.left_action_items.append(
                    md_app_bar.right_action_items[0])
                md_app_bar.right_action_items = []
            else:
                left_action_items = md_app_bar.left_action_items
                action_items = left_action_items[0:2]
                md_app_bar.right_action_items = [left_action_items[-1]]
                md_app_bar.left_action_items = action_items

    def set_error_message(self, *args):
        """Checks text of TextField with type "on_error"
        for the screen TextFields."""

        if len(self.root.ids.text_field_error.text) == 2:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

    def set_list_md_icons(self, text='', search=False):
        """Builds a list of icons for the screen MDIcons."""

        def add_icon_item(name_icon):
            self.main_widget.ids.scr_mngr.get_screen(
                'md icons').ids.rv.data.append(
                {
                    'viewclass': 'MDIconItemForMdIconsList',
                    'icon': name_icon,
                    'text': name_icon,
                    'callback': self.callback_for_menu_items
                }
            )

        self.main_widget.ids.scr_mngr.get_screen('md icons').ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

    def set_menu_for_demo_apps1(self):
        if not len(self.app.menu_for_demo_apps):
            for name_item in self.app.demo_apps_list:
                self.app.menu_for_demo_apps.append(
                    {'viewclass': 'OneLineListItem',
                     'text': name_item,
                     'on_release': lambda x=name_item: self.show_demo_apps(name_item)})

    def on_pause(self):
        return True

    def on_stop(self):
        pass

    def open_settings(self, *args):
        return False


class ContentForAnimCard(BoxLayout):
    callback = ObjectProperty(lambda x: None)


class BaseFanScreen(MDFanScreen):
    path_to_image = StringProperty()


class ScreenOne(BaseFanScreen):
    pass


class ScreenTwo(BaseFanScreen):
    pass


class ScreenTree(BaseFanScreen):
    pass


class ScreenFour(BaseFanScreen):
    pass


class AvatarSampleWidget(ILeftBody, Image):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


class PopupScreen(MDPopupScreen):
    pass


class ImageTouch(CircularRippleBehavior, ButtonBehavior, Image):
    pass


class MyCard(MDCard):
    text = StringProperty('')


if __name__ == '__main__':
    KitchenSink().run()

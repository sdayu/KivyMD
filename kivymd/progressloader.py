# -*- coding: utf-8 -*-

"""
Progress Loader
===============

Copyright © 2010-2018 HeaTTheatR

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Progressbar downloads files from the server.

Example
-------

import os

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.progressloader import MDProgressLoader
from kivymd.theming import ThemeManager
from kivymd.toast import toast


Builder.load_string('''
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDRoundFlatIconButton kivymd.button.MDRoundFlatIconButton


<Root@BoxLayout>
    orientation: 'vertical'
    spacing: dp(5)

    MDToolbar:
        id: toolbar
        title: 'MD Progress Loader'
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color

    FloatLayout:
        id: box

        MDRoundFlatIconButton:
            text: "Download file"
            icon: "download"
            pos_hint: {'center_x': .5, 'center_y': .6}
            on_release: app.show_example_download_file()
''')


class Test(App):
    theme_cls = ThemeManager()

    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

    def build(self):
        self.main_widget = Factory.Root()
        return self.main_widget

    def set_chevron_back_screen(self):
        '''Sets the return chevron to the previous screen in ToolBar.'''

        self.main_widget.ids.toolbar.right_action_items = []

    def download_progress_hide(self, instance_progress, value):
        '''Hides progress progress.'''

        self.main_widget.ids.toolbar.right_action_items =\
            [['download',
                lambda x: self.download_progress_show(instance_progress)]]

    def download_progress_show(self, instance_progress):
        self.set_chevron_back_screen()
        instance_progress.open()
        instance_progress.animation_progress_from_fade()

    def show_example_download_file(self):
        link = 'https://www.python.org/ftp/python/3.5.1/python-3.5.1-embed-win32.zip'
        progress = MDProgressLoader(
            url_on_image=link,
            path_to_file=os.path.join(self.directory, 'python-3.5.1.zip'),
            download_complete=self.download_complete,
            download_hide=self.download_progress_hide
        )
        progress.start(self.main_widget.ids.box)

    def download_complete(self):
        self.set_chevron_back_screen()
        toast('Done')


Test().run()
"""

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty

from kivymd.cards import MDCard

Builder.load_string('''
#:import Window kivy.core.window.Window
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDLabel kivymd.label.MDLabel
#:import MDCard kivymd.cards.MDCard


<MDProgressLoader>
    pos: (Window.width // 2) - (self.width // 2), (Window.height // 2) - (self.height // 2)
    size_hint_y: None
    size_hint_x: .8
    height: spinner.height + dp(20)
    spacing: dp(10)
    padding: dp(10)

    canvas:
        Color:
            rgba: app.theme_cls.primary_color
        Rectangle:
            size: self.size
            pos: self.pos

    MDSpinner
        id: spinner
        size_hint: None, None
        size: dp(46), dp(46)
        color: 1, 1, 1, 1

    MDLabel:
        id: label_download
        shorten: True
        max_lines: 1
        halign: 'left'
        valign: 'top'
        text_size: self.width, None
        size_hint_y: None
        height: spinner.height
        size_hint_x: .8
        text: 'Download...'

    Widget:
        size_hint_x: .1
''')


class MDProgressLoader(MDCard):
    path_to_file = StringProperty()
    '''The path to which the uploaded file will be saved.'''

    url_on_image = StringProperty()
    '''Link to uploaded file.'''

    label_download = StringProperty('Download')
    '''Signature of the downloaded file.'''

    download_complete = ObjectProperty()
    '''Function, called after a successful file upload.'''

    download_hide = ObjectProperty(lambda x: None)
    '''Function that is called when the download window is closed.'''

    download_flag = BooleanProperty(False)
    '''If True - the download process is in progress.'''

    def __init__(self, **kwargs):
        super(MDProgressLoader, self).__init__(**kwargs)
        self.root_instance = None

    def start(self, root_instance):
        self.root_instance = root_instance
        self.download_flag = True
        self.root_instance.add_widget(self)
        self.retrieve_progress_load(self.url_on_image, self.path_to_file)
        Clock.schedule_once(self.animation_progress_to_fade, 2.5)

    def open(self):
        self.animation_progress_from_fade()

    def draw_progress(self, percent):
        """
        :type percent: int;
        :param percent: loading percentage;

        """

        self.ids.label_download.text = '%s: %d %%'\
                                       % (self.label_download, percent)

    def animation_progress_to_fade(self, interval):
        if not self.download_flag:
            return

        animation = Animation(
            center_y=Window.height, center_x=Window.width,
            opacity=0, d=.2, t='out_quad'
        )
        animation.bind(on_complete=lambda x, y: self.download_hide(self, None))
        animation.start(self)

    def animation_progress_from_fade(self):
        animation = Animation(
            center_y=Window.height // 2, center_x=Window.width // 2,
            opacity=1, d=.2, t='out_quad'
        )
        animation.start(self)
        Clock.schedule_once(self.animation_progress_to_fade, 2.5)

    def retrieve_progress_load(self, url, path):
        """
        :type url: str;
        :param url: link to content;

        :type path: str;
        :param path: path to save content;
        """

        req = UrlRequest(
            url, on_progress=self.update_progress, chunk_size=1024,
            on_success=self.on_success, file_path=path)

    def update_progress(self, request, current_size, total_size):
        percent = current_size * 100 // total_size
        self.draw_progress(percent)

    def on_success(self, req, result):
        self.root_instance.remove_widget(self)
        self.download_complete()
        self.download_flag = False

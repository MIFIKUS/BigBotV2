from l2m_ui_funcs.actions_in_menus.classes import classes
from l2m_ui_funcs.actions_in_menus.aghathions import aghathions
from l2m_ui_funcs.main_screen import open_classes_menu, open_menu, open_aghathions_menu

from main_funcs.windows import switch_windows


def fuse_classes():
    open_menu()
    open_classes_menu()

    classes.open_fuses_list()

    while classes.auto_select() is not False:
        print('Нажат автовыбор')
        classes.fuse()
        print('Нажата кнопка фьюза')
        classes.show_all()
        print('Нажата кнопка показать все')

        if classes.go_to_result_available():
            print('Есть кнопка перейти к результату')
            classes.go_to_result()
            print('Нажал на кнопку перейти к результату')

        while classes.repeat_available():
            print('Есть возможность повтора')
            classes.repeat()
            print('Повтор')
            if classes.go_to_result_available():
                print('Есть кнопка перейти к результату')
                classes.go_to_result()
                print('Нажал на кнопку перейти к результату')
            print('Нажата кнопка показать все')
            classes.show_all()
        classes.exit_fuse()

        classes.reopen_fuse_menu()

    if classes.confirm_red_available():
        classes.open_confirm_list()
        classes.confirm_all()

    classes.exit_classes_menu()


def fuse_aghations():
    open_menu()
    open_aghathions_menu()

    aghathions.open_fuses_list()

    while aghathions.auto_select() is not False:
        aghathions.fuse()
        aghathions.show_all()

        while aghathions.repeat_available():
            aghathions.repeat()
        aghathions.exit_fuse()

        aghathions.reopen_fuse_menu()

    if aghathions.confirm_red_available():
        aghathions.open_confirm_list()
        aghathions.confirm_all()

    aghathions.exit_aghathions_menu()


def run():
    fuse_classes()
    fuse_aghations()


def start():
    switch_windows(run)

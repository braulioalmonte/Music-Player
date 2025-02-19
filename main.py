import flet as ft
from objects import appWidth,appHeight,baseColor,View

def main(page: ft.Page):
    # CONFIG
    page.title = "Student ID Card"
    page.window.width = appWidth
    page.window.height = appHeight
    page.bgcolor = baseColor

    # ROUTING
    def route_change(route):
        page.views.clear()
        match(page.route):
            case _:
                pass
            #     View("/home",HomeContent()).set(page)
        
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # STARTING PAGE
    page.go("/home")

ft.app(target=main,assets_dir="assets")
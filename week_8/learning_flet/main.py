import flet as ft

def main(page: ft.Page):
    page.title ="Learning FLET"
    content = ft.Column(
        spacing=20,
        controls=[
            ft.Text("This is a sample Flet application",size=32, weight="w600"),
            ft.Text("Welcome to learning FLET", size=16),
            ft.Row(
                spacing=20,
                controls=[
                    ft.Text("This is a row"),
                    ft.ElevatedButton("Click Me!")
                ]
                
            )
        ], 
    )

    # DISPLAY OUR SCREEN
    page.add(content)

ft.app(target=main)    
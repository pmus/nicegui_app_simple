#pip3 install nicegui


from nicegui import app, ui, Client
import os

#app.native.window_args['frameless'] = True 

style_main = "pt-4 pb-4 min-h-fit min-w-fit bg-white"
style_text_main = "justify-start no-underline p-0.5 gap-0.5 py-3 px-3 bg-white pr-10"
style_h1_left = "text-2xl gray px-3 text-start font-geologica pb-0 mb-0 font-bold t-2xl"
style_button_yellow = "text-black bg-yellow w-33 border-yes"

async def button_clicked(some):
    ui.notify('Желтая кнопка нажата')

@ui.page("/")
async def page_index() -> None:
    container = ui.row().classes(style_main)
    with container:
        ui.html("Привет").classes(style_h1_left)
        ui.separator()
        text_main1 = ui.html("""<p>Это пример.<br>
            Графической программы.</p>""").classes(style_text_main)
        ui.separator()
        button_action = ui.button("С кнопкой", on_click=button_clicked)
        button_action.classes(style_button_yellow)
        button_action.props('icon-right=arrow_forward')

""" Run server """
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Example", native=True)

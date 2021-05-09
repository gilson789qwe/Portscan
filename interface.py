import tkinter as tk


def janela() -> tk.Tk:
    tela = tk.Tk()
    tela.title("PortScan")
    tela.config(padx=10, pady=10, background="#fff")
    tela.resizable(False, False) #janela não será redimencionada
    return tela

def ip_label(tela) -> tk.Label:
    l = tk.Label(
    tela, text='Endereço', 
    anchor='e', justify='right', background='#fff'
    )
    l.grid(row=0, column=0, columnspan=5, sticky='news',padx=(0,230))
    return l
def ip_display(tela) -> tk.Entry:
    d = tk.Entry(tela)
    d.grid(row=0, column=1, columnspan=5, sticky='news')
    d.config(
        font=('Helvetica', 10, 'bold'),
        justify='left', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    #d.bind('<Control-a>', display_control_a) #Vai fazer um evento q ocorrer dentro da janela
    #Esse bind('<control-a') # é o bind do click normal do mouse
def porta_label(tela) -> tk.Label:
    l = tk.Label(
    tela, text='Porta', 
    anchor='e', justify='right', background='#fff'
    )
    l.grid(row=1, column=0, columnspan=5, sticky='news',padx=(0,250))
    return l
def porta_display(tela) -> tk.Entry:
    d = tk.Entry(tela)
    d.grid(row=1, column=1, columnspan=5, sticky='news')
    d.config(
        font=('Helvetica', 10, 'bold'),
        justify='left', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    #d.bind('<Control-a>', display_control_a) #Vai fazer um evento q ocorrer dentro da janela
    #Esse bind('<control-a') # é o bind do click normal do mouse
    return d
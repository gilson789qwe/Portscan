from interface import janela, ip_label, ip_display, porta_label, \
    porta_display

def principal():
    tela = janela()
    label_ip = ip_label(tela)
    display_ip = ip_display(tela)
    label_porta = porta_label(tela)
    display_porta=porta_display(tela)
    tela.mainloop()
    
if __name__ == '__main__':
    principal()
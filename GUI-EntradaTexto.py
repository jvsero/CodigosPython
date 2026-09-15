from tkinter import *

window = Tk()
window.title("Exemplo de botão")

# Cria um rótulo
lbl = Label(window, text="Olá")
lbl.grid(column=0, row=0)

# Cria a caixa de input (Entry)
txt = Entry(window, width=100)
txt.grid(column=0, row=1)


# Função que será chamada quando o botão for clicado
def clicked():
  # Pega o texto digitado na caixa e atualiza o rótulo
  user_text = txt.get()
  lbl.configure(text=f"Olá, {user_text}")


# Cria um botão
btn = Button(window, text="Clique em mim", command=clicked)
btn.grid(column=1, row=1)

window.mainloop()

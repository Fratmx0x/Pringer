# Definizione dei menu
foodmenu = {1: 'COOKIES', 2: 'CHEESECAKE', 3: 'MUFFIN', 4: 'LEMONPIE'}
drinkmenu = {5: 'CHOCOLATE', 6: 'MOCACCINO', 7: 'SUCCHI DI FRUTTA'}

carrello = []
clienti = []  # Lista per registrare i clienti


def mostra_menu():
    """Mostra il menu dei cibi e delle bevande."""
    print('\nMENU FOOD:')
    for numero, prodotto in foodmenu.items():
        print(f'{numero}: {prodotto}')
    
    print('\nMENU DRINK:')
    for numero, prodotto in drinkmenu.items():
        print(f'{numero}: {prodotto}')


def aggiungi_al_carrello():
    """Permette all'utente di aggiungere prodotti al carrello."""
    print("\nAggiungi i prodotti uno alla volta attraverso i numeri, usa 0 per terminare l'ordine.")
    
    while True:
        try:
            prodotticarrello = int(input("Numero del prodotto: "))
            
            if prodotticarrello == 0:
                break
            elif prodotticarrello in foodmenu:
                carrello.append(foodmenu[prodotticarrello])
                print(f'{foodmenu[prodotticarrello]} aggiunto al carrello!')
            elif prodotticarrello in drinkmenu:
                carrello.append(drinkmenu[prodotticarrello])
                print(f'{drinkmenu[prodotticarrello]} aggiunto al carrello!')
            else:
                print("Numero non valido, riprova.")
        
        except ValueError:
            print("Errore: inserisci un numero valido.")


def mostra_carrello():
    """Mostra i prodotti attualmente nel carrello."""
    print('\nOra il tuo carrello contiene:')
    if not carrello:
        print('- Il carrello è vuoto!')
    else:
        for item in carrello:
            print(f'- {item}')
    print('\nFantastico, ordine inviato! <3')


def registrazione_cliente():
    """Permette di registrare un nuovo cliente."""
    print("\nVuoi entrare a far parte della Pringer's family e accedere alle nostre offerte riservate?")
    risposta = input("(si/no): ").strip().lower()

    if risposta == 'si':
        print('Fantastico! <3 Dunque...')

        nome = input('Come ti chiami? ').strip()
        data_nascita = input('Qual è la tua data di nascita? (Formato: DD-MM-YYYY) ').strip()
        telefono = input('Quasi finito, ora ci serve il numero di telefono: ').strip()
        email = input('E la mail: ').strip()

        cliente = {
            "nome": nome,
            "data_di_nascita": data_nascita,
            "telefono": telefono,
            "email": email
        }

        clienti.append(cliente)  # Salva il cliente nella lista

        print(f'\nGrazie {nome}! Ora avrai accesso a tutte le nostre offerte riservate ai membri della Pringer\'s family.')
        print("E il giorno del tuo compleanno ti aspettiamo per festeggiare insieme con un regalo! ")
    else:
        print('Magari la prossima volta!')


# Inizio del programma
print('Ciao e benvenuto da Pringer!')
print('Mi chiamo FraBot e sono qui per aiutarti :)')

# Chiedi se mostrare il menu
if input('\nVuoi aprire il menù? (si/no): ').strip().lower() == 'si':
    mostra_menu()

# Aggiunta prodotti al carrello
aggiungi_al_carrello()

# Mostra il carrello
mostra_carrello()

# Registrazione cliente
registrazione_cliente()

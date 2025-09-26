import tkinter as tk
from tkinter import messagebox
from tacheDB import create_task, get_all_tasks, update_task, delete_task

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Ma Liste de Taches")
fenetre.geometry("600x500")
fenetre.configure(bg="lightblue")

# Variables globales
tache_selectionnee = None

# Fonction pour ajouter une tache
def ajouter_tache():
    texte = champ_texte.get()
    if texte == "":
        messagebox.showwarning("Attention", "Veuillez ecrire une tache")
        return
    
    try:
        create_task(texte, "Medium", "En cours")
        champ_texte.delete(0, tk.END)
        afficher_taches()
        messagebox.showinfo("Succes", "Tache ajoutee!")
    except Exception as e:
        messagebox.showerror("Erreur", "Probleme: " + str(e))

# Fonction pour afficher les taches
def afficher_taches():
    # Vider la liste
    liste_taches.delete(0, tk.END)
    
    try:
        taches = get_all_tasks()
        for tache in taches:
            id, contenu, status, priorite = tache
            texte_affiche = f"[{id}] {contenu} - {status} - {priorite}"
            liste_taches.insert(tk.END, texte_affiche)
    except Exception as e:
        messagebox.showerror("Erreur", "Probleme: " + str(e))

# Fonction pour selectionner une tache
def selectionner_tache():
    global tache_selectionnee
    selection = liste_taches.curselection()
    if selection:
        tache_selectionnee = selection[0]
        messagebox.showinfo("Selection", "Tache selectionnee")

# Fonction pour supprimer une tache
def supprimer_tache():
    global tache_selectionnee
    if tache_selectionnee is None:
        messagebox.showwarning("Attention", "Choisissez une tache")
        return
    
    try:
        taches = get_all_tasks()
        if tache_selectionnee < len(taches):
            id_tache = taches[tache_selectionnee][0]
            delete_task(id_tache)
            afficher_taches()
            tache_selectionnee = None
            messagebox.showinfo("Succes", "Tache supprimee!")
    except Exception as e:
        messagebox.showerror("Erreur", "Probleme: " + str(e))

# Fonction pour marquer comme terminee
def terminer_tache():
    global tache_selectionnee
    if tache_selectionnee is None:
        messagebox.showwarning("Attention", "Choisissez une tache")
        return
    
    try:
        taches = get_all_tasks()
        if tache_selectionnee < len(taches):
            id_tache, contenu, status, priorite = taches[tache_selectionnee]
            update_task(id_tache, contenu, priorite, "Terminée")
            afficher_taches()
            messagebox.showinfo("Succes", "Tache terminee!")
    except Exception as e:
        messagebox.showerror("Erreur", "Probleme: " + str(e))

# Interface utilisateur
titre = tk.Label(fenetre, text="Ma Liste de Taches", font=("Arial", 20, "bold"), bg="lightblue")
titre.pack(pady=10)

# Champ de saisie
frame_saisie = tk.Frame(fenetre, bg="lightblue")
frame_saisie.pack(pady=10)

label_texte = tk.Label(frame_saisie, text="Nouvelle tache:", font=("Arial", 12), bg="lightblue")
label_texte.pack(side=tk.LEFT)

champ_texte = tk.Entry(frame_saisie, font=("Arial", 12), width=30)
champ_texte.pack(side=tk.LEFT, padx=5)

bouton_ajouter = tk.Button(frame_saisie, text="Ajouter", command=ajouter_tache, bg="green", fg="white", font=("Arial", 10))
bouton_ajouter.pack(side=tk.LEFT, padx=5)

# Liste des taches
label_liste = tk.Label(fenetre, text="Mes taches:", font=("Arial", 14, "bold"), bg="lightblue")
label_liste.pack(pady=(20, 5))

liste_taches = tk.Listbox(fenetre, font=("Arial", 11), height=15, width=70)
liste_taches.pack(pady=5)

# Boutons d'action
frame_boutons = tk.Frame(fenetre, bg="lightblue")
frame_boutons.pack(pady=10)

bouton_selectionner = tk.Button(frame_boutons, text="Selectionner", command=selectionner_tache, bg="blue", fg="white", font=("Arial", 10))
bouton_selectionner.pack(side=tk.LEFT, padx=5)

bouton_terminer = tk.Button(frame_boutons, text="Terminer", command=terminer_tache, bg="orange", fg="white", font=("Arial", 10))
bouton_terminer.pack(side=tk.LEFT, padx=5)

bouton_supprimer = tk.Button(frame_boutons, text="Supprimer", command=supprimer_tache, bg="red", fg="white", font=("Arial", 10))
bouton_supprimer.pack(side=tk.LEFT, padx=5)

bouton_actualiser = tk.Button(frame_boutons, text="Actualiser", command=afficher_taches, bg="purple", fg="white", font=("Arial", 10))
bouton_actualiser.pack(side=tk.LEFT, padx=5)

# Charger les taches au demarrage
afficher_taches()

# Lancer l'application
fenetre.mainloop()

#!/usr/bin/env python3
"""
CLI Todo App - Día 1 Proyecto Python
Diego - USIL Ingeniería Software 6to ciclo
"""

from pathlib import Path
from typing import List
import sys


def load_tasks() -> List[str]:
    """Carga tareas desde tasks.txt"""
    tasks_file = Path.cwd() / "tasks.txt"
    if tasks_file.exists():
        return tasks_file.read_text(encoding="utf-8").splitlines()
    return []


def save_tasks(tasks: List[str]) -> None:
    """Guarda lista de tareas en tasks.txt"""
    tasks_file = Path.cwd() / "tasks.txt"
    tasks_file.write_text("\n".join(tasks), encoding="utf-8")


def add_task(tasks: List[str], new_task: str) -> List[str]:
    """Agrega nueva tarea al final de la lista"""
    tasks.append(new_task)
    return tasks


def print_tasks(tasks: List[str]) -> None:
    """Imprime tareas numeradas"""
    if not tasks:
        print("📭 Sin tareas")
        return
    print("📋 Tus tareas:")
    for i, task in enumerate(tasks, 1):
        print(f" {i}. {task}")


def main():
    """Función principal - maneja comandos CLI"""
    if len(sys.argv) < 2:
        print("❌ Uso: python -m todo [add|list][del][complete][help][clear]")
        return
    
    command = sys.argv[1]
    tasks = load_tasks()
    
    if command == "add" and len(sys.argv) > 2:
        new_task = " ".join(sys.argv[2:])
        tasks = add_task(tasks, new_task)
        save_tasks(tasks)
        print(f"✅ '{new_task}' agregada")
    
    elif command == "list":
        print_tasks(tasks)
    
    elif command == "del" and len(sys.argv) > 2:
        try:
            numero = int(sys.argv[2]) - 1
            if 0 <= numero  < len(tasks):
                tarea_borrada = tasks.pop(numero)
                save_tasks(tasks)
                print(f"🗑️ Tarea '{tarea_borrada}' eliminada")
            else:
                print("❌ Número de tarea inválido")
        except ValueError:
            print("❌ El número de tarea debe ser un número entero")
    
    elif command == "complete" and len(sys.argv) > 2:
        try:
            numero = int(sys.argv[2]) - 1
            if 0 <= numero < len(tasks):
                tasks[numero] = f"✅ {tasks[numero]}"
                save_tasks(tasks)
                print(f"🎉 Tarea {numero+1} completada")
            else:
                print("❌ Número de tarea inválido")
        except ValueError:
                print("❌ Uso: complete NÚMERO")
    
    elif command == "clear":                           # ①
        tasks = [t for t in tasks if not t.startswith("✅")]  # ②
        save_tasks(tasks)                      # ③
        print(f"🧹 {len(tasks)} tareas restantes")  # ④

    
    elif command == "help":
        print("""
    🆘 CLI Todo v3.0 - Diego

    python todo/cli.py COMANDO

    📋 list              → Lista tareas
    ➕ add "texto"       → Nueva tarea  
    🗑️ del N            → Borra #N
    ✅ complete N        → Marca #N ✓
    ❓ help              → Esta ayuda
    🧹 clear             → Borra tareas completadas
    """)
    return

if __name__ == "__main__":
    main()

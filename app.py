import pymem
import pymem.process

while True:
    try:
        print("\nAttaching to game.....\n================================================================")
        process = pymem.Pymem("cs2.exe") # finding game process
        break
    except pymem.exception.ProcessNotFound:
        print("\nError trying again\n================================================================")

client = pymem.process.module_from_name(pm.process_handle, "client.dll") # attaching the process handle

dwLocalPlayerController = pm.read_longlong(client.lpBaseOfDll + 0x19038F8) # geting the local player controller
dwLocalPlayerPawn = pm.read_longlong(client.lpBaseOfDll + 0x1729348) # geting the local player pawn
print("\nRewriting game memory...\n================================================================")

#fov
pm.write_int(dwLocalPlayerController + 0x6CC, 120) # rewriting game memory for local player controller

#anti-flash
pm.write_int(dwLocalPlayerPawn + 0x14C8, 100) # rewriting game memory for local player pawn
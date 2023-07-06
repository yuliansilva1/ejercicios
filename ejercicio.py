import funciones as fn
while True:
    fn.ver_menu()
    opc = fn.validar_opcion()
    if opc==1:
        fn.registrar_cliente()
    elif opc==2:
        fn.suscripcion()
    elif opc==3:
        fn.consultar_datos_cliente()
    elif opc==4:
        fn.eliminar_cliente()
    else:
        print("gracias por suscribirse")
        break
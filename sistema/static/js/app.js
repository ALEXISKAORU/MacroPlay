$("#cambiar_contrasenia").validate({
    "errorClass": "is-invalidate",
    "rules":{
        password:{
            required: true,
            minlength: 8,
            maxlength: 15
        },
        re_password:{
            equalTo:"#password"
        }
    },
    "messages":{
        password:{
            required: "La contraseña es obligatoria",
            minlength: "El minimo de caracteres es de 8",
            maxlength: "El maximo de caracteres es de 15"
        },
        re_password:{
            equalTo:"Las contraseñas deben ser iguales"
        }
    }
})

$("#añadir_juego").validate({
    "errorClass": "is-invalidate",
    "rules":{
        titulo:{
            required: true,
            maxlength: 150
        },
        genero:{
            required: true,
            maxlength: 50
        },
        anio:{
            required: true
        },
        precio:{
            required: true
        },
        clasificacion:{
            required: true,
            maxlength: 50
        },
        stock:{
            required: true
        },
        resenia:{
            required: true,
            maxlength: 250
        }
    },
    "messages":{
        titulo:{
            required: "El titulo es obligatorio",
            maxlength: "El maximo de caracteres es de 150"
        },
        genero:{
            required: "El genero es obligatorio",
            maxlength: "El maximo de caracteres es de 50"
        },
        anio:{
            required: "El año es obligatorio"
        },
        precio:{
            required: "El precio es obligatorio"
        },
        clasificacion:{
            required: "La clasificacion es obligatoria",
            maxlength: "El maximo de caracteres es de 50"
        },
        stock:{
            required: "La stock es obligatoria"
        },
        resenia:{
            required: "La reseña es obligatoria",
            maxlength: "El maximo de caracteres es de 250"
        }
    }
})

$("#crear_macroplayers").validate({
    "errorClass": "is-invalidate",
    "rules":{
        first_name:{
            required: true
        },
        last_name:{
            required: true
        },
        email:{
            required: true
        },
        username:{
            required: true,
            minlength: 3,
            maxlength: 15
        },
        password:{
            required: true,
            minlength: 8,
            maxlength: 15
        },
    },
    "messages":{
        first_name:{
            required: "El nombre es obligatorio"
        },
        last_name:{
            required: "El apellido es obligatorio"
        },
        email:{
            required: "El email es obligatorio"

        },
        username:{
            required: "El nombre de usuario es obligatorio",
            minlength: "El minimo de caracteres es de 3",
            maxlength: "El maximo de caracteres es de 15"
        },
        password:{
            required: "La contraseña es obligatoria",
            minlength: "El minimo de caracteres es de 8",
            maxlength: "El maximo de caracteres es de 15"
        }
    }
})

$("#editar_juego").validate({
    "errorClass": "is-invalidate",
    "rules":{
        titulo:{
            required: true,
            maxlength: 150
        },
        genero:{
            required: true,
            maxlength: 50
        },
        anio:{
            required: true
        },
        precio:{
            required: true
        },
        clasificacion:{
            required: true,
            maxlength: 50
        },
        stock:{
            required: true
        },
        resenia:{
            required: true,
            maxlength: 250
        }
    },
    "messages":{
        titulo:{
            required: "El titulo es obligatorio",
            maxlength: "El maximo de caracteres es de 150"
        },
        genero:{
            required: "El genero es obligatorio",
            maxlength: "El maximo de caracteres es de 50"
        },
        anio:{
            required: "El año es obligatorio"
        },
        precio:{
            required: "El precio es obligatorio"
        },
        clasificacion:{
            required: "La clasificacion es obligatoria",
            maxlength: "El maximo de caracteres es de 50"
        },
        stock:{
            required: "La stock es obligatoria"
        },
        resenia:{
            required: "La reseña es obligatoria",
            maxlength: "El maximo de caracteres es de 250"
        }
    }
})
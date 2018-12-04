let table = $('#tablaAlumnos').DataTable({
        "ajax": {
            "url": "/api/alumnos/",
            "type": "GET"
        },
        "columns": [
            {"data": "id"},
            {"data": "nombre"},
            {"data": "apellido_pat"},
            {"data": "apellido_mat"},
            {"data": "rut"},
            {"data": "sexo"},
            {"data": "email"},
            {"data": "telefono"},
            {"data": "direccion"},
            {"data": "universidadProcedencia"},
            {"data": "posee"},
            {"data": "nivelacion"},
            {"data": "resultadosNivelacion"},
            {"data": "semestreIngreso"},
            {"data": "anioIngreso"},
            {"data": "estadoMatricula"},
            {"data": "antecedentesAcademicos"},
            {"data": "antecedentesProfesionales"},
            {"data": "cartaRecomendacion"},
            {"data": "entrevista"},
            {"data": "puntaje"},
            {"data": "resultadosCondicion"},
            {
                "data": null,
                "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
                '<button type="button" class="btn btn-danger">Delete</button>'
            }
        ]
    });

let table = $('#tablaProfesores').DataTable({
        "ajax": {
            "url": "/api/profesores/",
            "type": "GET"
        },
        "columns": [
            {"data": "id"},
            {"data": "nombre"},
            {"data": "apellido_pat"},
            {"data": "apellido_mat"},
            {"data": "rut"},
            {"data": "sexo"},
            {"data": "email"},
            {"data": "telefono"},
            {"data": "direccion"},
            {"data": "profesion"},
            {"data": "cursosImpartados"},
            {
                "data": null,
                "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
                '<button type="button" class="btn btn-danger">Delete</button>'
            }
        ]
    });

let table = $('#tablaUsuarios').DataTable({
        "ajax": {
            "url": "/api/users/",
            "type": "GET"
        },
        "columns": [
            {"data": "id"},
            {"data": "username"},
            {"data": "first_name"},
            {"data": "last_name"},
            {"data": "email"},
            {"data": "is_active"},
            {"data": "is_staff"},
            {
                "data": null,
                "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
                '<button type="button" class="btn btn-danger">Delete</button>'
            }
        ]
    });
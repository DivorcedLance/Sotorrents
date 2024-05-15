# Resume

## Semana 01

### Conceptos Básicos

#### Dato

Es un registro discreto que proporciona información. Puede ser un número, una palabra, una imagen, etc.

#### Información

Datos que han sido procesados en forma intangible. Es decir, datos que han sido organizados, interpretados y presentados de manera significativa.

##### Cualidades
- Precisa
- Oportuna
- Plena
- Significativa
- Coherente
- Segura

##### Objetivos
Transmisión de conocimiento para la investigación, planificación y la toma de decisiones.

##### Fuentes:
Primarias : Observación, Experimentos, Encuestas, Estimaciones subjetivas.
Secundarias : Informes propios y externos.

#### Conocimiento:

Los datos son hechos aislados que al ser procesados se convierten en información. La información, al ser procesada se convierte en conocimiento.

#### Modelos de datos

Conjunto de herramientas conceptuales para describir los datos, relaciones entre ellos, semántica asociada a los datos y restricciones de consistencia.

##### Tipos

- Modelos Lógicos basados en Objetos
  - Modelo Entidad-Relación
  - Modelo Orientado a Objetos

- Modelos Lógicos basados en Registros
  - Modelo Relacional
  - Modelo Jerárquico
  - Modelo de Red
- Modelos Físicos

#### SGBD

Niveles:

- Nivel Externo: Vista
- Nivel Logico: Esquema
- Nivel Interno: Almacenamiento

Entorno:

- Programas de aplicación y procesadores de lenguaje de aplicación.
- Herramientas de Gestión.
- Sistema de Diccionario de Datos.
- Sistemas Operativo y de Gestión de ficheros
- Protocolos y Sistemas Distribuidos

##### Funciones:

En el contexto de las bases de datos, hay tres funciones principales que definen cómo interactuamos y gestionamos los datos. Estas funciones se llevan a cabo a través de diferentes sublenguajes del SQL (Structured Query Language). A continuación, definiré claramente cada función y los lenguajes asociados:

###### 1. Función de Descripción

####### Lenguaje de Definición de Datos (LDD)

- **Descripción**: Esta función se encarga de definir y modificar la estructura de la base de datos y sus objetos, como tablas, índices, y restricciones de integridad. Incluye la especificación de cómo se organizarán los datos y cómo se relacionarán entre sí.
  
- **Operaciones Principales**: 
  - **CREATE**: Para crear nuevas tablas, vistas, índices, entre otros.
  - **ALTER**: Para modificar estructuras existentes, como añadir o eliminar columnas en una tabla.
  - **DROP**: Para eliminar elementos existentes de la base de datos.

- **Propósito**: Establecer la arquitectura y esquemas de la base de datos, asegurando que los datos estén correctamente organizados y que se respeten las relaciones y restricciones necesarias para mantener la integridad y el orden.

###### 2. Función de Manipulación

####### Lenguaje de Manipulación de Datos (LMD)

- **Descripción**: Esta función permite realizar operaciones sobre los datos almacenados en la base de datos. Facilita la inserción, modificación, eliminación y consulta de datos.
  
- **Operaciones Principales**: 
  - **SELECT**: Para consultar y recuperar datos.
  - **INSERT**: Para añadir nuevos registros a las tablas.
  - **UPDATE**: Para modificar registros existentes.
  - **DELETE**: Para eliminar registros.

- **Propósito**: Permitir a los usuarios interactuar con los datos, ya sea para agregar nuevos registros, modificar los existentes, eliminarlos o simplemente consultarlos para obtener la información necesaria.

###### 3. Función de Utilización

####### Lenguaje de Control de Datos (LCD)

- **Descripción**: Esta función gestiona los derechos y permisos de acceso a la base de datos para garantizar la seguridad y controlar quién puede realizar qué operaciones sobre los datos y la estructura de la base de datos.
  
- **Operaciones Principales**: 
  - **GRANT**: Para otorgar derechos y permisos a los usuarios.
  - **REVOKE**: Para retirar derechos y permisos previamente otorgados.

- **Propósito**: Asegurar que solo los usuarios autorizados tengan acceso a realizar ciertas acciones en la base de datos, como acceder a datos específicos, realizar cambios estructurales, o manipular los datos de acuerdo con sus roles y necesidades.




| Prefijo | Acceso usuario        | Contenido                          | Notas                                                                 |
|---------|----------------------|------------------------------------|-----------------------------------------------------------------------|
| DBA_    | Administradores      | Todos los objetos                  | Algunas vistas agregan información útil para los administradores.     |
| ALL_    | Todos los usuarios   | Objetos a los cuales tiene acceso un usuario | Incluye objetos que son propiedad del usuario.                        |
| USER_   | Todos los usuarios   | Objetos propiedad del usuario       | Las vistas omiten el atributo owner, se muestra información relacionada con el usuario que consulta.           |


Esquemas en Bases de Datos
- Un clúster de bases de datos contiene una o más bases de datos con un nombre asociado.
- Usuarios y grupos de usuarios se comparten en el clúster pero no se comparte nada más entre las bases de datos.
- Un cliente que se conecta al servidor de bases de datos solo puede acceder a los datos de la base de datos a la que se conectó.
- Por ejemplo, si quisiera conectarse a una base conteniendo información de usuario centralizada (login único) y luego acceder a una base de datos usada por un software particular, debería realizar dos conexiones.

# Base de Datos

Esquemas en Bases de Datos
- Un clúster de bases de datos contiene una o más bases de datos con un nombre asociado.
- Usuarios y grupos de usuarios se comparten en el clúster pero no se comparte nada más entre las bases de datos.
- Un cliente que se conecta al servidor de bases de datos solo puede acceder a los datos de la base de datos a la que se conectó.
- Por ejemplo, si quisiera conectarse a una base conteniendo información de usuario centralizada (login único) y luego acceder a una base de datos usada por un software particular, debería realizar dos conexiones.


## Modelo lógico vs modelo conceptual

 El modelo de datos lógicos es una representación abstracta de una posible implementación, sin estar vinculado a ninguna implementación específica, mientras que el modelo de datos conceptual es una representación de alto nivel de los requisitos comerciales y los conjuntos y relaciones de datos conectados. El modelo lógico, a través de un proceso de normalización, brinda una representación más estructurada de las entidades y sus relaciones y detalla más sus relaciones y características: se resuelven las redundancias, las relaciones de muchos a muchos, las ambigüedades y las incertidumbres de atribución de entidades y surge obviamente una posible implementación de base de datos.


 
# Notas de clase

## Organizacion de datos

### 1. Secuencial

**Almacena y ordena** los archivos en bloques contiguos en memoria. La informacion procesada y los datos se almacenan en un solo bloque.

Estos registros pueden estar organizadas de alguna manera, la busqueda de informacion se hace de inicio a fin, y los resultados se guardan al final.

Por ejemplo, si tengo 20 registros, tengo que leer del 1 al 19 para llear al 20.

No puedo insertar nuevos elementos, sino que me toca mover los presentes y de ahi insertarlo. NO REESCRIBIBLE

| Ventajas | Desventajas |
| --- | --- |
| Faciles de programar y diseñar | Es un proceso que consume tiempo | 
|Se usa cuando un numero largo de registro debe ser accedido, notas o factura| Tiene alta redundancia de datos, genera multiples copias| 



### 2. Acceso directo/ Random Accesss
| Ventajas | Desventajas |
| --- | --- |
|  No es necesario organizar los registros | Es compleja de implementar, por los altos niveles de complejidad desde software| 
|Accede a los registros deseados de manera inmediata| | 

### 3. Indexed sequential access

Combina el acceso directo y el secuencial. En este, los registros se almacenan **aleatoriamente**, puede acceder de manera secuencial o aleatoriamente usando el indice. EL indice esta almacenado en un archivo.

| Ventajas | Desventajas |
| --- | --- |
|  El acceso secuencial y aleatorio es posibke | Requiere llaves e indicees unicos y reorganizacion periodica| 
| Los archivos pueden ser ingresados en la mitad del archivo |  Requiere mas espacio de almacenamiento| 

## Archivos secuenciales en Java

Las clases que se usan para el tratamiento de ficheros estan ubicadas en el paquete **java.io** por lo que deben ser importadas.

### Manejo de excepciones

En java existen **excepciones comprobadas**, que obligan al programa a no cerrarse tras encontrar error

Bloque de codigo **Try - catch**

```java
try {
    //Bloque de codigo

} catch ( error){
    // Respuesta al error correspondiente

}
```

## Operaciones con archivos/ficheros

- Apertura: Se abre el archivo y se prepara para leerlo o escribirlo.
- Cierre: Libera el fichero e indica que se finalizaron las operaciones

Se sobre entiende, leer, escribir, sobre escribir, etc.

### Apertura y cierre de un fichero

Se reserva el fichero para operar con el. Se establece un fluho de datos entre el fichero a una variable en java. Es sobre esa variable que se realizan las operaciones en el archivo.

Para esto utilizamos la clase **file**. Que nos permite realizar multiples operaciones en el archivo en relacion a su ruta, mas no escbirir sobre este.

### La clase file

El constructor de la clase file tiene el siguiente esquema 

```java
File variableArchivo = new File("ruta archivo");
```

La variable es un objeto con los datos del fichero, la ruta de este puede ser absoluta o relativa. Con esta clase puedo trabajar sobre los meta datos del fichero pero no editarlo ni leerlo como tal. Tenemos metodos como:

```java
variableArchivo.getName();
variableArchivo.getPath();
```

### Clase file reader

Esta clase trabaja sobre un objeto de tipo file, es decir, sobre la variable de tipo file. Pero solo permite de caracter a caracter

```java
FileReader variableArchivo = new FileReader(variableArchivo);
```

### Clase file buffer

Ya con esta clsde podemos leer linea por linea, utilizando la funcion de **BufferReader**, llamada **readLine()**. Si la linea existe devuelve la linea, sino, devuelve null. 

```java
String linea = buffer.readLine();
```

Por el funcionamiento de readLine(), podemos leer con el siguiente ciclo simple todo el archivo.

```java
String LINEA;
while((LINEA = buffer.readLine()) != null){

    System.out.println(LINEA);
}
```

## Escritura en archivos en java

Utilizamos ```FileWriter``` y ```BufferedWriter```, los cuales utilizaremos para escribir en el archivo. El objeto de bufferedwriter sera el que haga todo.

```java
FileWriter outFile = new FileWriter(rutaArchivo);
BufferedWriter bw = new BufferedWriter (outFile);
```

Tenemos acceso a distintos comandos, como :

```java
bw.write();
bw.newLine();
```


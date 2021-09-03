import mysql.connector
import hashlib

class Insecto:

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def save_avistamiento(self, data, data_avist, data_foto, avistamientos, fotos):
        # Inclusión de datos en la tabla de avistamiento:

        sql_avistamiento = """
            INSERT INTO avistamiento (comuna_id, dia_hora, sector, nombre, email, celular)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        self.cursor.execute(sql_avistamiento, data)
        self.db.commit()        # Modificación de la base de datos.

        last_avistamiento_id = "SELECT id FROM `avistamiento` ORDER BY id DESC LIMIT 1"
        self.cursor.execute(last_avistamiento_id)
        last_id = self.cursor.fetchall()[0][0]

        # Inclusión del detalle del avistamiento.
        det_ids = []
        for k in range(avistamientos):
            sql_detalle_a = """
                INSERT INTO detalle_avistamiento (dia_hora, tipo, estado, avistamiento_id)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(sql_detalle_a, (*data_avist[3*k:3*k+3], last_id))
            self.db.commit()  # Modificación de la base de datos.

            last_det_avistamiento_id = "SELECT id FROM `detalle_avistamiento` ORDER BY id DESC LIMIT 1"
            self.cursor.execute(last_det_avistamiento_id)
            last_det = self.cursor.fetchall()[0][0]
            det_ids.append(last_det)

        # Inclusión de las fotos del detalle del avistamiento.
        index_det_id = 0 # Inicializador para la selección del id del detalle del avistamiento
        foto_id = 0
        for i in fotos:
            det_id = det_ids[index_det_id]
            for j in range(i):
                fileitem = data_foto[foto_id]
                foto_name = fileitem.filename
                # Creación del archivo Hash
                sql_count = " SELECT COUNT(id) FROM foto"
                self.cursor.execute(sql_count)
                total = self.cursor.fetchall()[0][0] + 1  # Parametro sensible, utilizar hash para reducir el riesgo

                hash_archivo = str(total) + hashlib.sha256(foto_name.encode()).hexdigest()[:20]
                # print(hash_archivo)
                # print(foto_name)
                self.photo_path = hash_archivo

                # Guardado de archivos
                open("media/" + hash_archivo + ".jpg", "wb").write(fileitem.file.read())

                sql_foto = """
                                    INSERT INTO foto (ruta_archivo, nombre_archivo, detalle_avistamiento_id)
                                    VALUES (%s, %s, %s)
                        """
                self.cursor.execute(sql_foto, (hash_archivo, foto_name, det_id))  # Ejecución de la consulta
                self.db.commit()  # modifico la base de datos
                foto_id += 1
            index_det_id += 1

    def get_info(self, tablename):
        sql_info =f"""
            SELECT * FROM {tablename} 
        """
        self.cursor.execute(sql_info)
        return  self.cursor.fetchall()  # Se obtiene la data de la tabla solicitada.

    # Función para obtener información que esten almacenadas en diferentes tablas.
    def cross_info(self, tablename, atribute_1, atribute_2, cross_value):

        sql_cross = f"""
            SELECT {atribute_1} FROM {tablename} WHERE {atribute_2}='{cross_value}'"""
        self.cursor.execute(sql_cross)
        return self.cursor.fetchall()
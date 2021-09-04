package dcc.cc5002.model;

import java.sql.*;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;

public class Tarea4DB {

    private Connection conn;

    public Tarea4DB(String db, String user, String pass) throws ClassNotFoundException, SQLException {
        Class.forName("com.mysql.cj.jdbc.Driver");
        this.conn = DriverManager.getConnection("jdbc:mysql://localhost/"+ db +"?" +
                "user="+ user +"&password="+ pass +"");

    }

    public ResultSet getTotalData(String table) throws SQLException {
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM "+ table +" ORDER BY id DESC ");
        return rs;
    }

    public ResultSet getPartialData(String table, String column, String value) throws SQLException {
        Statement stmt_2 = conn.createStatement();
        ResultSet rs_2 = stmt_2.executeQuery("SELECT * FROM "+ table +" WHERE "+ column +"=" + value + " ORDER BY id DESC");
        return rs_2;
    }

    public void close() throws SQLException {
        this.conn.close();
    }

    public static String getDate() {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
        LocalDateTime now = LocalDateTime.now();
        return dtf.format(now);
    }

        public void insertData(String date, String comment, String note, String photo) throws SQLException {
        PreparedStatement ps = conn.prepareStatement(
                "INSERT INTO comentario_foto (fecha, comentario, nota, foto_bicho)" +
                        "VALUES (?, ?, ?, ?)"

        );
        ps.setString(1, date);
        ps.setString(2, comment);
        ps.setString(3, note);
        ps.setString(4, photo);
        ps.executeUpdate();
        this.close();

    }
}


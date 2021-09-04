package dcc.cc5002.controller;

import dcc.cc5002.model.Tarea4DB;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.SQLException;

public class Tarea_4Servlet extends HttpServlet {

    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        request.setCharacterEncoding("UTF-8");
        String date = request.getParameter("Date");
        String comment = request.getParameter("Comment");
        String note = request.getParameter("Note");
        String photo = request.getParameter("Photo");

        Tarea4DB tarea4 = null;
        try {
            tarea4 = new Tarea4DB("tarea2", "root", "");
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }

        try {
            tarea4.insertData(date, comment, note, photo);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        request.setAttribute("tarea4", tarea4);
        request.getRequestDispatcher("index.jsp").forward(request, response);

    }


}
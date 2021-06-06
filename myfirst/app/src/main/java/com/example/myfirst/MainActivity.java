package com.example.myfirst;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    public void onClick(View view){
        Button login = findViewById(R.id.login);
        }
    }


    public void signUpClicked(View view){
        EditText user = findViewById(R.id.user);
        EditText pass = findViewById(R.id.pass);

        if (user.getText().toString().matches("")|| pass.getText().toString().matches(""))
            Toast.makeText(this,"Your Roll no. and a password is required",Toast.LENGTH_SHORT).show();
    }else{
        ParseUser u = new ParseUser();
        u.setUsername(user.getText().toString());
        u.setPassword(pass.getText().toString());


    }




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}

package com.example.nelicia.opicapplication;

import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Random;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private Random random;
    private ArrayList<String> korean;
    private ArrayList<String> english;
    private int nowIndex;
    private TextView koreanTextView;
    private TextView englishTextView;
    private String[] nowText;
    private int maxTextSize;
    private int nowCount;
    private int[] checkArray;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        korean=new ArrayList<String>();
        english=new ArrayList<String>();
        nowText=new String[2];
        random=new Random();
        nowCount=0;

        FileInputStream fis = null;
        try {
            fis = new FileInputStream("storage/extSdCard/opic/setting.set");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(fis));


        String temp = "";
        String[] tempStringArray=new String[2];
        try {
            while ((temp = bufferedReader.readLine()) != null) {
                Log.i("log",temp);
                tempStringArray=temp.split("  ");
                english.add(tempStringArray[0]);
                korean.add(tempStringArray[1]);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        maxTextSize=korean.size();
        checkArray=new int[maxTextSize];

        koreanTextView=(TextView)findViewById(R.id.korean);
        englishTextView=(TextView)findViewById(R.id.english);
        Button nextButton=(Button)findViewById(R.id.nextbutton);
        Button solution=(Button)findViewById(R.id.solution);
        nextButton.setOnClickListener(this);
        solution.setOnClickListener(this);


    }

    @Override
    public void onClick(View v) {
        switch(v.getId())
        {
            case R.id.nextbutton:
                if(nowCount==maxTextSize)
                {
                    nowCount=0;
                    for(int i=0;i<checkArray.length;i++)
                    {
                        checkArray[i]=0;
                    }
                }
                while(true) {
                    nowIndex = random.nextInt(100);
                    if (nowIndex < korean.size() && checkArray[nowIndex]==0) {
                        nowCount++;
                        checkArray[nowIndex]=1;
                        nowText[0]=english.get(nowIndex);
                        nowText[1]=korean.get(nowIndex)+"("+nowCount+"/"+maxTextSize+")";
                        Log.i("nowIndex0:",nowText[0]);
                        Log.i("nowIndex1:",nowText[1]);
                        koreanTextView.setText(nowText[1]);
                        englishTextView.setText("답변");
                        break;
                    }
                }
                break;
            case R.id.solution:
                englishTextView.setText(nowText[0]);
                break;
        }
    }
}

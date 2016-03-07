package com.example.controller3;

import android.content.Context;
import android.graphics.Color;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.LinearLayout.LayoutParams;
import android.widget.TextView;

public class CustomEditText extends LinearLayout{

	private EditText editText;
	private TextView textView;
	
	public CustomEditText(Context context,int width,int height,int ems,String name) {
		super(context);
		// TODO Auto-generated constructor stub
		setLayoutParams(new LayoutParams(width,height));
		
		textView=new TextView(context);
		textView.setText(name);
		addView(textView);
		
		//setBackgroundColor(Color.BLUE);
		editText=new EditText(context);
		//editText.setHeight(LayoutParams.WRAP_CONTENT);
		//editText.setWidth(LayoutParams.MATCH_PARENT);
		editText.setEms(ems);
		addView(editText);
		
	}
	
	public void setLayoutSize(int width,int height)
	{
		setLayoutParams(new LayoutParams(width, height));
	}
	
	public String getText()
	{
		return editText.getText().toString();
	}
	public void setText(String str)
	{
		editText.setText(str);
	}
	

}

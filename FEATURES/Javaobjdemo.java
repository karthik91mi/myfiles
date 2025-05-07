class Student
{
	int sno;
	String name;
	float marks;
	String cname;
}//Student--class name--Programmer-Defined Data Type

class  Javaobjdemo
{
	public static void main(String[] args) 
	{
		Student s=new Student();
		s.sno=100;
		s.name="Rossum";
		s.marks=22.22f;
		System.out.println(s.sno+"   "+s.name+"  "+s.marks);
		s.cname="OUCET";
		System.out.println(s.sno+"   "+s.name+"  "+s.marks+" "+s.cname);
		s.addr="HYD";
	}
}

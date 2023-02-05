## java
* 基本类型 byte + short + int + long;
* 基本类型 char + boolean 
* 基本类型 float + double
### class 
* static 不能使用this;实例化之前就创建;可以直接class调用
* public(公用)>protect(父子+同包)+默认(同包)+priovate(内部使用)
* 子类重写父类方法时，访问权限不可更严格，权限从小到大为:private->默认->protected->public
* 重载=>同名函数如果参数数量，参数类型，或者顺序不一样，称为重载
### interface 
* abstract类(包含abstract属性的class)
* 全部属性和方法都是abstract的class称为interface（interface内部都是抽象属性）
* 接口通过implements修饰
* interface中的属性都是常量,使用public static final修饰,不写也是
* 接口中的方法都用 public abstract修饰
* java8之后可以使用默认方法(default)和静态方法(static); static方法直接使用interface调用
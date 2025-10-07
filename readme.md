# Youbot Başlangıç


## SSH bağlantıları

1. Jetson SSH kullanıcı adı ve şifresi

    `ssh jetson@192.168.1.20` 

2. Youbot SSH kullanıcı adı ve şifresi

    `ssh sinan@192.168.1.10` 

**Bilgisayarların saati eşleşmediği zaman tflerin zamanları ile alakalı sıkıntı oluyor bu yüzden bunları eşitlemekte yarar var**  `ntp update 192.168.1.30`


## Robotu başlatma

1. Rosore

    Roscore için jetsonu kullanıyoruz bu yüzden jetson terminalinde
    `roscore` ile ros çekirdeğini başlatıyoruz
2. Youbot'u Başlatma  
    Youbot terminalinden youbotun ros sürücüsünü başlatıyoruz                                                                             
    `roslaunch youbot_driver_ros_interface youbot_driver.launch`  
3. Zed kamerayı başlatma
   
    Zedin eksen takımları youbot driverında başlatılan urdfte tanımlı olduğundan 
    
    `roslaunch zed_wrapper zed_no_tf.launch`

    (eğer zed youbot açık değilken kullanılmak istenirse     `roslaunch zed_wrapper zed.launch`)


## Kumanda ile Robotu sürme
   \+ tuşu tüm ros nodelarını kapatır.  
   R tuşu Dead Man's switch görevü görmektedir. Basılı tutulduğunda robot hareket ettirebilir öbür türlü çalışmayacaktır.  
   Sol analog y ekseni ileri yönde hareket ettir.  
   Sol analog x ekseni dönme hareketinii yaptırır.  
   Sağ analog x ekseni yatay yönde hareket ettirir.          
    **Kumandayı başlatmak için :**        
   `roslaunch teleop_twist_joy teleop.launch`
## Kol test etme 
## Rtabmap
## Rviz

   
 



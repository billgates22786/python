import java.util.Scanner;
class Month
{
    public static void main(String[] args)
    {
        int month;
        Scanner input = new Scanner(System. in);
        System.out.print("ENTER THE MONTH NUMBER:- ");
        month = input.nextInt();
       if (month==1) 
    {
        System.out.println("January has 31 days.\n Some extra info January, the first month of the Gregorian calendar, marks the beginning of the new year. It typically embodies a sense of renewal and fresh starts, symbolizing hope and resolutions. With winter's chill, January often features snowy landscapes and is a time for reflection, goal-setting, and planning ahead.\n");
    } 
    else if (month==2) 
    {
        System.out.println("February has 28 or 29 days.\nSome extra info February, the shortest month, holds significance with Valentine's Day, celebrating love and affection. It marks a transition from winter to spring, often featuring unpredictable weather. February's highlight is the leap year occurrence, adding a 29th day every four years. It embodies themes of love, renewal, and anticipation for the coming spring.\n");
    } 
    else if (month==3) 
    {
        System.out.println("March has 31 days.\n Some extra info March, the third month of the year, signals the onset of spring in the Northern Hemisphere, bringing longer days and warmer weather. It represents rebirth and rejuvenation, with blooming flowers and emerging foliage. March hosts various cultural celebrations like St. Patrick's Day, symbolizing diversity and the promise of new beginnings.\n");
    } 
    else if (month==4) 
    {
        System.out.println("April has 30 days.\nSome extra info April: April signifies the full arrival of spring, with blossoming flowers and warming temperatures. It embodies growth and vitality, often associated with Easter celebrations and the promise of new life.\n");
    } 
    else if (month==5) 
    {
        System.out.println("May has 31 days.\n Some extra info May: May welcomes the full bloom of spring, with vibrant colors and lush foliage. It represents abundance and fertility, featuring holidays like Mother's Day and Memorial Day, honoring life and sacrifice.\n");
    } 
    else if (month==6) 
    {
        System.out.println("June has 30 days.\n Some extra info June: June marks the beginning of summer, with longer days and balmy temperatures. It embodies vitality and leisure, often associated with weddings and outdoor activities, fostering a sense of joy and relaxation.\n");
    } 
    else if (month==7) 
    {
        System.out.println("July has 31 days.\n Some extra info July: July epitomizes the peak of summer, with warm weather and outdoor festivities. It represents freedom and independence, highlighted by patriotic celebrations like Independence Day in the United States.\n");
    } 
    else if (month==8) 
    {
        System.out.println("August has 31 days.\n Some extra info August: August signifies the height of summer, with sultry temperatures and lazy days. It embodies relaxation and reflection, offering a respite before the return to routine in the fall.\n");
    } 
    else if (month==9) 
    {
        System.out.println("September has 30 days.\n Some extra info September: September marks the transition from summer to fall, with cooling temperatures and changing foliage. It symbolizes new beginnings, as schools resume and nature prepares for the harvest season.\n");
    } 
    else if (month==10) 
    {
        System.out.println("October has 31 days.\n Some extra info October: October heralds the arrival of autumn, with crisp air and vibrant foliage. It embodies coziness and nostalgia, featuring Halloween festivities and the anticipation of harvest gatherings.\n");
    } 
    else if (month==11) 
    {
        System.out.println("November has 30 days.\n Some extra info November: November embodies the essence of fall, with golden leaves and brisk winds. It represents gratitude and reflection, featuring holidays like Thanksgiving, where families gather to give thanks and share meals.\n");
    } 
    else if (month==12) 
    {
        System.out.println("December has 31 days.\n Some extra info December: December brings the festive spirit of the holiday season, with celebrations like Christmas and Hanukkah illuminating the winter darkness. It symbolizes joy and togetherness, marking the end of the year with warmth and goodwill.\n");
    } 
    else 
    {
        System.out.println("check the month number you duffer.\n Wow, you must be using a different calendar. In this one, there are 12 months in a year \n");
    }
    }
}


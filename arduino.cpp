#include <Mouse.h>

unsigned long jkiss_x = 123456789;
unsigned long jkiss_y = 234567891;
unsigned long jkiss_z = 345678912;
unsigned long jkiss_w = 456789123;
unsigned long jkiss_c = 0;

unsigned long jkiss32() {
    jkiss_y ^= jkiss_y << 5;
    jkiss_y ^= jkiss_y >> 7;
    jkiss_y ^= jkiss_y << 22;
    long t = jkiss_z + jkiss_w + jkiss_c;
    jkiss_z = jkiss_w;
    jkiss_c = t < 0;
    jkiss_w = t & 2147483647;
    jkiss_x += 1411392427;
    return jkiss_x + jkiss_y + jkiss_w;
}

unsigned long jkiss32Seed(unsigned long seed) {
    if (seed != 0) {
        jkiss_x = 123456789;
        jkiss_y = seed;
        jkiss_z = 345678912;
        jkiss_w = 456789123;
        jkiss_c = 0;
    }
    return jkiss_y;
}

unsigned long jkiss32Random(unsigned long min, unsigned long max) {
    return min + (jkiss32() % ((max - min) + 1));
}

void setup() {
    Serial.begin(9600);
    Mouse.begin();
    
    while (!Serial);

    Serial.print("jkiss32 seed:");
    Serial.println(jkiss32Seed(micros()));
}

float sampleAverageLightOverTime(int ms) {
    float average = 0.0f;
    unsigned long counter = 1;
    unsigned long microsStart = micros();
    unsigned long microsFinish = microsStart + (ms * 1000);
    do {
        float value = (float)analogRead(A1);
        average += (value - average) / counter;
        counter++;
    } while (micros() < microsFinish);
    return average;
}

float lerp(float a, float b, float t) {
    return a * (1.0f - t) + (b * t);
}

void loop() {
    // Calibrate
    Mouse.move(0, 100);
    delay(250);
    float dark = sampleAverageLightOverTime(500);
    Mouse.move(0, -100);
    delay(250);
    float bright = sampleAverageLightOverTime(500);
    if (bright - dark < 200) {
        if (dark > bright)
            Serial.println("Invalid dark and bright measurements");
        else
            Serial.println("Dark and bright measurements are too similar");
        delay(2000);
        return;
    }
    int darkThreshold = (int)(lerp(dark, bright, 0.05f) + 1.0f);
    int brightThreshold = (int)lerp(dark, bright, 0.2f);
    int confirmationThreshold = (int)lerp(dark, bright, 0.8f);

    // Collect results
    unsigned long results[250];
    int numResults = 0;
    for (; numResults < 250; numResults++) {
        Mouse.move(0, 100);
        while (analogRead(A1) > darkThreshold);

        // Make sure we don't synchronize ourselves to the display...
        // NOTE: don't go over (2^14)-1 because of delayMicroseconds limitation
        delayMicroseconds(jkiss32Random(5500, 13000));
        
        unsigned long microsStart = micros();
        Mouse.move(0, -100);
        while (analogRead(A1) < brightThreshold);
        unsigned long microsFinish = micros();
        
        delay(16);
        if (analogRead(A1) < confirmationThreshold) {
            Serial.println("Confirmation threshold not reached");
            break;
        }

        unsigned long microsDelta = microsFinish - microsStart;
        results[numResults] = microsDelta;
    }

    // Print results
    for (int i = 0; i < numResults; i++) {
        unsigned long decimal = results[i] % 1000;
        unsigned long millisDelta = (results[i] - decimal) / 1000;
        Serial.print(millisDelta);
        if (decimal < 10)
            Serial.print(".00");
        else if (decimal < 100)
            Serial.print(".0");
        else
            Serial.print(".");
        Serial.print(decimal);
        Serial.print(",");
    }
    Serial.println("");
}

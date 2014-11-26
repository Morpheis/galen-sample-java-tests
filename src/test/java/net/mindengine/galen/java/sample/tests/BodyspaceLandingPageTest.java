package net.mindengine.galen.java.sample.tests;

import net.mindengine.galen.java.sample.components.NewGalenTestBase;
import org.testng.annotations.Test;

import java.io.IOException;

public class BodyspaceLandingPageTest extends NewGalenTestBase {

    @Test(dataProvider = "devices")
    public void bodyspaceLandingPage_shouldLookGood_onDevice(TestDevice device) throws IOException {
        load("/");
        checkLayout(driver, "/specs/header.spec", device.getTags());
    }
}

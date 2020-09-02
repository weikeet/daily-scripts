package net.appcloudbox.autopilot;

/**
 * @author weicools
 * @date 2020.09.02
 */
public class AutopilotEvent {
    public AutopilotEvent() {
    }

    public static void logTopicEvent(String topicID, String eventName) {
        logTopicEvent(topicID, eventName, (Double) null);
    }

    public static void logTopicEvent(String topicID, String eventName, Double eventValue) {
        AutopilotSDK.getInstance().getTopic(topicID).logEvent(eventName, eventValue);
    }

    public static void logAppEvent(String eventName) {
        logAppEvent(eventName, (Double) null);
    }

    public static void onActive() {
        AutopilotSDK.getInstance().getAppEventLogger().logActive();
    }

    public static void logAppEvent(String eventName, Double eventValue) {
        AutopilotSDK.getInstance().getAppEventLogger().logEvent(eventName, eventValue);
    }

    public static void onExtendedActive() {
        AutopilotSDK.getInstance().getAppEventLogger().logExtendedActive();
    }

    public static void onAdShow() {
        AutopilotSDK.getInstance().getAppEventLogger().logAdShow();
    }

    public static void onAdClick(int adType, String network) {
        AutopilotSDK.getInstance().getAppEventLogger().logAdClick(adType, network);
    }

    public static void onIAP(double value) {
        AutopilotSDK.getInstance().getAppEventLogger().logIAP(value);
    }

    public static void onOccasionActionPerformed(AutopilotOccasionAction action) {
        action.logPerform();
    }
}

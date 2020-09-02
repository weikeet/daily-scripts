package net.appcloudbox.autopilot;

import android.app.Application;
import android.content.Context;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;

import net.appcloudbox.autopilot.core.AutopilotProvider;
import net.appcloudbox.autopilot.utils.CollectionUtils;
import net.appcloudbox.autopilot.utils.ContentProviderUtils;

import java.util.Iterator;
import java.util.List;

/**
 * @author weicools
 * @date 2020.09.02
 */
public class AutopilotConfig {
    public static final String ACTION_CONFIG_FETCH_FINISHED = "net.appcloudbox.autopilot.CONFIG_FETCH_FINISHED";

    public static final String ACTION_TOPICS_READY_TO_PRELOAD_RESOURCE = "net.appcloudbox.autopilot.TOPICS_READY_TO_PRELOAD_RESOURCE";

    public static final String ACTION_SHOW_RTOT_ALTER = "ACTION_SHOW_RTOT_ALTER";

    public static final String EXTRA_UPDATE_TOPICS = "EXTRA_UPDATE_TOPICS";

    public static final String EXTRA_RESULT = "EXTRA_RESULT";

    public AutopilotConfig() {
    }

    public static void initialize(@NonNull Application application, @NonNull AutopilotSessionController sessionController) {
        AutopilotSDK.getInstance().initialize((new AutopilotInitOption.Builder(application, sessionController)).build());
    }

    public static void initialize(@NonNull Application application, @NonNull List<String> activityNameBlackList) {
        AutopilotSDK.getInstance().initialize((new AutopilotInitOption.Builder(application, activityNameBlackList)).build());
    }

    public static void setIsUpgradeUser() {
        AutopilotSDK.getInstance().getUserProperty().setIsUpgradeUser();
    }

    public static void setRtotAutoShow(boolean isAuto) {
        AutopilotSDK.getInstance().getRtotPopup().setRtotAutoShow(isAuto);
    }

    public static void setCustomerUserId(Context context, String customerUserId) {
        AutopilotSDK.getInstance().getUserProperty().setCustomerUserId(context, customerUserId);
    }

    public static void setIsGdprConsentGranted(Context context, boolean isGdprConsentGranted) {
        AutopilotSDK.getInstance().getUserProperty().setIsGdprConsentGranted(context, isGdprConsentGranted);
    }

    public static void setAudienceProperty(String propertyName, String propertyValue) {
        AutopilotSDK.getInstance().getUserProperty().set(propertyName, propertyValue);
    }

    public static void setAudienceProperty(String propertyName, double propertyValue) {
        AutopilotSDK.getInstance().getUserProperty().set(propertyName, propertyValue);
    }

    public static void setAudienceProperty(String propertyName, boolean propertyValue) {
        AutopilotSDK.getInstance().getUserProperty().set(propertyName, propertyValue);
    }

    public static String getStringToTestNow(String topicID, String variationName, String defaultValue) {
        return AutopilotSDK.getInstance().getTopic(topicID).getString(variationName, defaultValue);
    }

    public static double getDoubleToTestNow(String topicID, String variationName, double defaultValue) {
        return AutopilotSDK.getInstance().getTopic(topicID).getDouble(variationName, defaultValue);
    }

    public static boolean getBooleanToTestNow(String topicID, String variationName, boolean defaultValue) {
        return AutopilotSDK.getInstance().getTopic(topicID).getBoolean(variationName, defaultValue);
    }

    public static AutopilotResource getResourceToTestNow(String topicID, String variationName, AutopilotResource defaultValue) {
        AutopilotResource resource = AutopilotSDK.getInstance().getTopic(topicID).getResource(variationName);
        return resource == null ? defaultValue : resource;
    }

    @NonNull
    public static AutopilotMembers getMembersToTestNow(String topicID, String variationName) {
        return AutopilotSDK.getInstance().getTopic(topicID).getMembers(variationName);
    }

    public static void clearResourceCache(String topicID) {
        AutopilotSDK.getInstance().getTopic(topicID).clearResourceCache();
    }

    public static void preloadResource(String topicID) {
        AutopilotSDK.getInstance().getTopic(topicID).preloadResource();
    }

    public static void setAutoPreloadTopics(@Nullable List<String> topicIDs) {
        if (!CollectionUtils.isEmpty(topicIDs)) {
            Iterator var1 = topicIDs.iterator();

            while (var1.hasNext()) {
                String topicID = (String) var1.next();
                AutopilotSDK.getInstance().getTopic(topicID).setAutoPreloadResource(true);
            }

        }
    }

    public static void showRtotAlert() {
        AutopilotSDK.getInstance().getRtotPopup().showRtotAlert();
    }

    public static boolean hasGotConfig(String topicID) {
        return AutopilotSDK.getInstance().getTopic(topicID).getStatus().hasGotVariation();
    }

    public static void onMarketingInfoReady(Context context) {
        ContentProviderUtils.asyncCall(context, AutopilotProvider.createContentUri(context), "CALL_REQUEST_REMOTE_CONFIG_FRAMEWORK", (String) null, (Bundle) null);
    }
}

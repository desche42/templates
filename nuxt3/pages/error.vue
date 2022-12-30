<template>
  <v-container>
    <v-card>
      <v-card-title>{{ $t("header") }}</v-card-title>
      <v-card-text>
        <p>{{ $t("content") }}</p>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  layout: "message",
};
</script>

<i18n>
{
  "en": {
    "header": "Authentication error",
    "content": "Please talk to the app admin if this problem persists"
  }
}
</i18n>

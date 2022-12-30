<template>
  <v-container>
    <v-card>
      <v-card-title>{{ $t("header") }}</v-card-title>
      <v-card-text>
        <p>{{ $t("content") }}</p>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" @click="toStartPage">{{ $t("button") }}</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {
  layout: "message",
  data() {
    return { url: "" };
  },
  methods: {
    toStartPage() {
      this.$router.push({ path: "/" });
    },
  },
};
</script>

<i18n>
  {
    "en": {
      "header": "Page not found",
      "content": "The page that you're looking for does not exist",
      "button": "Go to home page"
    }
  }
  </i18n>

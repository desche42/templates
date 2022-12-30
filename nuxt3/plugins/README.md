# PLUGINS

## Axios plugin

Catches request errors and success to handle them.

## Notifications

Uses `vue-notification` package to be able to display an alert using `this.$notify(configuration)`:

### Notification configuration

- [Package documentation](https://github.com/euvl/vue-notification/blob/master/README.md)

Example:

```js
  this.$notify({
    // (optional)
    // Name of the notification holder
    group: 'foo',

    // (optional)
    // Title (will be wrapped in div.notification-title)
    title: 'This is the <em>title</em>',

    // Content (will be wrapped in div.notification-content)
    text: 'This is some <b>content</b>',

    // (optional)
    // Class that will be assigned to the notification
    type: 'warn',

    // (optional, override)
    // Time (in ms) to keep the notification on screen
    duration: 10000,

    // (optional, override)
    // Time (in ms) to show / hide notifications
    speed: 1000,

    // (optional)
    // Data object that can be used in your template
    data: {}
  })
```

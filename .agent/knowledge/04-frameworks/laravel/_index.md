---
id: idx_laravel
resumo: Indice de recursos e manuais de laravel
gatilhos:
- frameworks
- laravel
- eloquent
- database
- http
- getting
- started
- console
- cashier
- collections
rotas:
- id: artisan
  resumo: '[!NOTE] Looking for hot reloading, multiline code editing, and autocompletion
    when interacting with your Laravel application? Check out [Tinkerwell](https://tinkerwell.app)!'
  gatilhos:
  - artisan
  - console
  - frameworks
  - laravel
  arquivo: ./artisan.md
  secoes:
  - introduction
  - writing-commands
  - defining-input-expectations
  - command-io
  - registering-commands
  - programmatically-executing-commands
  tokens_estimados: 8149
- id: authentication
  resumo: '[!NOTE] Guards and providers should not be confused with "roles" and "permissions".
    To learn more about authorizing user actions via permissions, please refer to
    the [authorization](/docs/{{version}}/authorization) documentation.'
  gatilhos:
  - authentication
  - frameworks
  - laravel
  arquivo: ./authentication.md
  secoes:
  - introduction
  - authentication-quickstart
  - manually-authenticating-users
  - http-basic-authentication
  - logging-out
  - password-confirmation
  tokens_estimados: 11632
- id: authorization
  resumo: '[!WARNING] Gates are a great way to learn the basics of Laravel''s authorization
    features; however, when building robust Laravel applications you should consider
    using [policies](#creating-policies) to organize your authorization rules.'
  gatilhos:
  - authorization
  - frameworks
  - laravel
  arquivo: ./authorization.md
  secoes:
  - introduction
  - gates
  - creating-policies
  - writing-policies
  - authorizing-actions-using-policies
  - authorization--inertia
  tokens_estimados: 8062
- id: billing
  resumo: '[!WARNING] To prevent breaking changes, Cashier uses a fixed Stripe API
    version. Cashier 16 utilizes Stripe API version `2025-06-30.basil`. The Stripe
    API version will be updated on minor releases in order to make use of new Stripe
    features and im...'
  gatilhos:
  - billing
  - cashier
  - frameworks
  - laravel
  - stripe
  arquivo: ./billing.md
  secoes:
  - introduction
  - upgrading-cashier
  - installation
  - configuration
  - quickstart
  - customers
  tokens_estimados: 28296
- id: blade
  resumo: '[!NOTE] Blade''s `{{ }}` echo statements are automatically sent through
    PHP''s `htmlspecialchars` function to prevent XSS attacks.'
  gatilhos:
  - blade
  - frameworks
  - laravel
  - templates
  arquivo: ./blade.md
  secoes:
  - introduction
  - displaying-data
  - blade-directives
  - components
  - anonymous-components
  - building-layouts
  tokens_estimados: 17454
- id: broadcasting
  resumo: '[!NOTE] Before diving into event broadcasting, make sure you have read
    Laravel''s documentation on [events and listeners](/docs/{{version}}/events).'
  gatilhos:
  - broadcasting
  - frameworks
  - laravel
  arquivo: ./broadcasting.md
  secoes:
  - introduction
  - quickstart
  - server-side-installation
  - client-side-installation
  - concept-overview
  - defining-broadcast-events
  tokens_estimados: 16928
- id: cache
  resumo: '[!NOTE] If you are using the Memcached driver, items that are stored "forever"
    may be removed when the cache reaches its size limit.'
  gatilhos:
  - cache
  - frameworks
  - laravel
  arquivo: ./cache.md
  secoes:
  - introduction
  - configuration
  - cache-usage
  - cache-tags
  - atomic-locks
  - cache-failover
  tokens_estimados: 7008
- id: cashier-paddle
  resumo: '[!WARNING] This documentation is for Cashier Paddle 2.x''s integration
    with Paddle Billing. If you''re still using Paddle Classic, you should use [Cashier
    Paddle 1.x](https://github.com/laravel/cashier-paddle/tree/1.x).'
  gatilhos:
  - cashier
  - frameworks
  - laravel
  - paddle
  arquivo: ./cashier-paddle.md
  secoes:
  - introduction
  - upgrading-cashier
  - installation
  - configuration
  - quickstart
  - checkout-sessions
  tokens_estimados: 16330
- id: collections
  resumo: '[!NOTE] The results of [Eloquent](/docs/{{version}}/eloquent) queries are
    always returned as `Collection` instances.'
  gatilhos:
  - collections
  - frameworks
  - laravel
  arquivo: ./collections.md
  secoes:
  - introduction
  - available-methods
  - method-listing
  - higher-order-messages
  - lazy-collections
  tokens_estimados: 28285
- id: concurrency
  resumo: Guia tecnico e referencias sobre Concurrency.
  gatilhos:
  - concurrency
  - frameworks
  - laravel
  arquivo: ./concurrency.md
  secoes:
  - introduction
  - running-concurrent-tasks
  - deferring-concurrent-tasks
  tokens_estimados: 727
- id: configuration
  resumo: '[!NOTE] Any variable in your `.env` file can be overridden by external
    environment variables such as server-level or system-level environment variables.'
  gatilhos:
  - configuration
  - frameworks
  - laravel
  arquivo: ./configuration.md
  secoes:
  - introduction
  - environment-configuration
  - accessing-configuration-values
  - configuration-caching
  - configuration-publishing
  - debug-mode
  tokens_estimados: 4735
- id: console-tests
  resumo: Guia tecnico e referencias sobre Console Tests.
  gatilhos:
  - console
  - frameworks
  - laravel
  - tests
  arquivo: ./console-tests.md
  secoes:
  - introduction
  - success--failure-expectations
  - input--output-expectations
  - console-events
  tokens_estimados: 1689
- id: container
  resumo: '[!NOTE] There is no need to bind classes into the container if they do
    not depend on any interfaces. The container does not need to be instructed on
    how to build these objects, since it can automatically resolve these objects using
    reflection.'
  gatilhos:
  - container
  - frameworks
  - laravel
  - service
  arquivo: ./container.md
  secoes:
  - introduction
  - binding
  - resolving
  - method-invocation-and-injection
  - container-events
  - psr-11
  tokens_estimados: 7017
- id: context
  resumo: '[!WARNING] If an object within the context is modified inside the scoped
    closure, that mutation will be reflected outside of the scope.'
  gatilhos:
  - context
  - frameworks
  - laravel
  arquivo: ./context.md
  secoes:
  - introduction
  - capturing-context
  - retrieving-context
  - removing-context
  - hidden-context
  - events
  tokens_estimados: 3674
- id: contracts
  resumo: Guia tecnico e referencias sobre Contracts.
  gatilhos:
  - contracts
  - frameworks
  - laravel
  arquivo: ./contracts.md
  secoes:
  - introduction
  - when-to-use-contracts
  - how-to-use-contracts
  - contract-reference
  tokens_estimados: 3781
- id: contributions
  resumo: Guia tecnico e referencias sobre Contribution Guide.
  gatilhos:
  - contribution
  - contributions
  - frameworks
  - guide
  - laravel
  arquivo: ./contributions.md
  secoes:
  - bug-reports
  - support-questions
  - core-development-discussion
  - which-branch
  - compiled-assets
  - security-vulnerabilities
  tokens_estimados: 2166
- id: controllers
  resumo: '[!NOTE] Controllers are not **required** to extend a base class. However,
    it is sometimes convenient to extend a base controller class that contains methods
    that should be shared across all of your controllers.'
  gatilhos:
  - controllers
  - frameworks
  - laravel
  arquivo: ./controllers.md
  secoes:
  - introduction
  - writing-controllers
  - controller-middleware
  - resource-controllers
  - dependency-injection-and-controllers
  tokens_estimados: 6782
- id: csrf
  resumo: '[!NOTE] For convenience, the CSRF middleware is automatically disabled
    for all routes when [running tests](/docs/{{version}}/testing).'
  gatilhos:
  - csrf
  - frameworks
  - laravel
  - protection
  arquivo: ./csrf.md
  secoes:
  - introduction
  - preventing-csrf-requests
  - x-csrf-token
  - x-xsrf-token
  tokens_estimados: 1571
- id: database-testing
  resumo: Guia tecnico e referencias sobre Database Testing.
  gatilhos:
  - database
  - frameworks
  - laravel
  - testing
  arquivo: ./database-testing.md
  secoes:
  - introduction
  - model-factories
  - running-seeders
  - available-assertions
  tokens_estimados: 2080
- id: database
  resumo: '[!NOTE] If you use the [Laravel installer](/docs/{{version}}/installation#creating-a-laravel-project)
    to create your Laravel application and select SQLite as your database, Laravel
    will automatically create a `database/database.sqlite` file and ru...'
  gatilhos:
  - database
  - frameworks
  - getting
  - laravel
  - started
  arquivo: ./database.md
  secoes:
  - introduction
  - running-sql-queries
  - database-transactions
  - connecting-to-the-database-cli
  - inspecting-your-databases
  - monitoring-your-databases
  tokens_estimados: 5366
- id: deployment
  resumo: '[!WARNING] If you execute the `config:cache` command during your deployment
    process, you should be sure that you are only calling the `env` function from
    within your configuration files. Once the configuration has been cached, the `.env`
    file will...'
  gatilhos:
  - deployment
  - frameworks
  - laravel
  arquivo: ./deployment.md
  secoes:
  - introduction
  - server-requirements
  - server-configuration
  - optimization
  - reloading-services
  - debug-mode
  tokens_estimados: 2656
- id: documentation
  resumo: Guia tecnico e referencias sobre Documentation.
  gatilhos:
  - documentation
  - frameworks
  - laravel
  arquivo: ./documentation.md
  secoes: []
  tokens_estimados: 1224
- id: dusk
  resumo: '[!WARNING] [Pest 4](https://pestphp.com/) now includes automated browser
    testing which offers significant performance and usability improvements compared
    to Laravel Dusk. For new projects, we recommend using Pest for browser testing.'
  gatilhos:
  - dusk
  - frameworks
  - laravel
  arquivo: ./dusk.md
  secoes:
  - introduction
  - installation
  - getting-started
  - browser-basics
  - interacting-with-elements
  - available-assertions
  tokens_estimados: 19586
- id: eloquent-collections
  resumo: 'Guia tecnico e referencias sobre Eloquent: Collections.'
  gatilhos:
  - collections
  - eloquent
  - frameworks
  - laravel
  arquivo: ./eloquent-collections.md
  secoes:
  - introduction
  - available-methods
  - custom-collections
  tokens_estimados: 3215
- id: eloquent-factories
  resumo: '[!NOTE] You can change your application''s Faker locale by updating the
    `faker_locale` option in your `config/app.php` configuration file.'
  gatilhos:
  - eloquent
  - factories
  - frameworks
  - laravel
  arquivo: ./eloquent-factories.md
  secoes:
  - introduction
  - defining-model-factories
  - creating-models-using-factories
  - factory-relationships
  tokens_estimados: 5564
- id: eloquent-mutators
  resumo: '[!NOTE] If you would like these computed values to be added to the array
    / JSON representations of your model, [you will need to append them](/docs/{{version}}/eloquent-serialization#appending-values-to-json).'
  gatilhos:
  - casting
  - eloquent
  - frameworks
  - laravel
  - mutators
  arquivo: ./eloquent-mutators.md
  secoes:
  - introduction
  - accessors-and-mutators
  - attribute-casting
  - custom-casts
  tokens_estimados: 8697
- id: eloquent-relationships
  resumo: '[!WARNING] Because PostgreSQL does not support executing the `MAX` function
    against UUID columns, it is not currently possible to use one-of-many relationships
    in combination with PostgreSQL UUID columns.'
  gatilhos:
  - eloquent
  - frameworks
  - laravel
  - relationships
  arquivo: ./eloquent-relationships.md
  secoes:
  - introduction
  - defining-relationships
  - many-to-many-relationships
  - polymorphic-relationships
  - querying-relations
  - aggregating-related-models
  tokens_estimados: 24176
- id: eloquent-resources
  resumo: '[!NOTE] This is a high-level overview of resources and resource collections.
    You are highly encouraged to read the other sections of this documentation to
    gain a deeper understanding of the customization and power offered to you by resources.'
  gatilhos:
  - api
  - eloquent
  - frameworks
  - laravel
  - resources
  arquivo: ./eloquent-resources.md
  secoes:
  - introduction
  - generating-resources
  - concept-overview
  - writing-resources
  - resource-responses
  tokens_estimados: 8202
- id: eloquent-serialization
  resumo: '[!NOTE] For an even more robust way of handling Eloquent model and collection
    JSON serialization, check out the documentation on [Eloquent API resources](/docs/{{version}}/eloquent-resources).'
  gatilhos:
  - eloquent
  - frameworks
  - laravel
  - serialization
  arquivo: ./eloquent-serialization.md
  secoes:
  - introduction
  - serializing-models-and-collections
  - hiding-attributes-from-json
  - appending-values-to-json
  - date-serialization
  tokens_estimados: 2120
- id: eloquent
  resumo: '[!NOTE] Before getting started, be sure to configure a database connection
    in your application''s `config/database.php` configuration file. For more information
    on configuring your database, check out [the database configuration documentation](/doc...'
  gatilhos:
  - eloquent
  - frameworks
  - getting
  - laravel
  - started
  arquivo: ./eloquent.md
  secoes:
  - introduction
  - generating-model-classes
  - eloquent-model-conventions
  - retrieving-models
  - retrieving-single-models--aggregates
  - inserting-and-updating-models
  tokens_estimados: 16893
- id: encryption
  resumo: Guia tecnico e referencias sobre Encryption.
  gatilhos:
  - encryption
  - frameworks
  - laravel
  arquivo: ./encryption.md
  secoes:
  - introduction
  - configuration
  - using-the-encrypter
  tokens_estimados: 1001
- id: envoy
  resumo: Guia tecnico e referencias sobre Laravel Envoy.
  gatilhos:
  - envoy
  - frameworks
  - laravel
  arquivo: ./envoy.md
  secoes:
  - introduction
  - installation
  - writing-tasks
  - running-tasks
  - notifications
  tokens_estimados: 2988
- id: errors
  resumo: '[!NOTE] To customize the exception reporting for a given exception, you
    may also utilize [reportable exceptions](/docs/{{version}}/errors#renderable-exceptions).'
  gatilhos:
  - error
  - errors
  - frameworks
  - handling
  - laravel
  arquivo: ./errors.md
  secoes:
  - introduction
  - configuration
  - handling-exceptions
  - http-exceptions
  tokens_estimados: 4879
- id: events
  resumo: '[!NOTE] Your event listeners may also type-hint any dependencies they need
    on their constructors. All event listeners are resolved via the Laravel [service
    container](/docs/{{version}}/container), so dependencies will be injected automatically.'
  gatilhos:
  - events
  - frameworks
  - laravel
  arquivo: ./events.md
  secoes:
  - introduction
  - generating-events-and-listeners
  - registering-events-and-listeners
  - defining-events
  - defining-listeners
  - queued-event-listeners
  tokens_estimados: 9093
- id: facades
  resumo: Guia tecnico e referencias sobre Facades.
  gatilhos:
  - facades
  - frameworks
  - laravel
  arquivo: ./facades.md
  secoes:
  - introduction
  - when-to-utilize-facades
  - how-facades-work
  - real-time-facades
  - facade-class-reference
  tokens_estimados: 4898
- id: filesystem
  resumo: '[!NOTE] You may configure as many disks as you like and may even have multiple
    disks that use the same driver.'
  gatilhos:
  - file
  - filesystem
  - frameworks
  - laravel
  - storage
  arquivo: ./filesystem.md
  secoes:
  - introduction
  - configuration
  - obtaining-disk-instances
  - retrieving-files
  - storing-files
  - deleting-files
  tokens_estimados: 8394
- id: folio
  resumo: Guia tecnico e referencias sobre Laravel Folio.
  gatilhos:
  - folio
  - frameworks
  - laravel
  arquivo: ./folio.md
  secoes:
  - introduction
  - installation
  - creating-routes
  - route-parameters
  - route-model-binding
  - render-hooks
  tokens_estimados: 2690
- id: fortify
  resumo: '[!NOTE] Remember, Fortify is a package that is meant to give you a head
    start implementing Laravel''s authentication features. **You are not required
    to use it.** You are always free to manually interact with Laravel''s authentication
    services by fo...'
  gatilhos:
  - fortify
  - frameworks
  - laravel
  arquivo: ./fortify.md
  secoes:
  - introduction
  - installation
  - authentication
  - two-factor-authentication
  - registration
  - password-reset
  tokens_estimados: 9062
- id: frontend
  resumo: '[!NOTE] For more detailed documentation on utilizing Vite with Laravel,
    please see our [dedicated documentation on bundling and compiling your assets](/docs/{{version}}/vite).'
  gatilhos:
  - frameworks
  - frontend
  - laravel
  arquivo: ./frontend.md
  secoes:
  - introduction
  - using-php
  - using-react-or-vue
  - bundling-assets
  tokens_estimados: 2777
- id: guia_pratico
  resumo: Guia tecnico e referencias sobre 💻 Exemplos Práticos Laravel - Guia Completo.
  gatilhos:
  - completo
  - exemplos
  - frameworks
  - guia
  - laravel
  - pratico
  arquivo: ./guia_pratico.md
  secoes:
  - classificação-de-tarefa
  - decisão-técnica
  - justificativa
  - análise-de-impacto
  - critérios-de-aceite
  - exemplos-por-categoria
  tokens_estimados: 6119
- id: hashing
  resumo: '[!NOTE] For more information on these options, please refer to the [official
    PHP documentation regarding Argon hashing](https://secure.php.net/manual/en/function.password-hash.php).'
  gatilhos:
  - frameworks
  - hashing
  - laravel
  arquivo: ./hashing.md
  secoes:
  - introduction
  - configuration
  - basic-usage
  - hash-algorithm-verification
  tokens_estimados: 1271
- id: helpers
  resumo: '[!NOTE] By default, the Laravel application skeleton does not include the
    `lang` directory. If you would like to customize Laravel''s language files, you
    may publish them via the `lang:publish` Artisan command.'
  gatilhos:
  - frameworks
  - helpers
  - laravel
  arquivo: ./helpers.md
  secoes:
  - introduction
  - available-methods
  - arrays--objects
  - numbers
  - paths
  - urls
  tokens_estimados: 24742
- id: homestead
  resumo: '[!WARNING] Laravel Homestead is a legacy package that is no longer actively
    maintained. [Laravel Sail](/docs/{{version}}/sail) may be used as a modern alternative.'
  gatilhos:
  - frameworks
  - homestead
  - laravel
  arquivo: ./homestead.md
  secoes:
  - introduction
  - installation-and-setup
  - updating-homestead
  - daily-usage
  - debugging-and-profiling
  - network-interfaces
  tokens_estimados: 8582
- id: horizon
  resumo: '[!NOTE] Before digging into Laravel Horizon, you should familiarize yourself
    with Laravel''s base [queue services](/docs/{{version}}/queues). Horizon augments
    Laravel''s queue with additional features that may be confusing if you are not
    already fam...'
  gatilhos:
  - frameworks
  - horizon
  - laravel
  arquivo: ./horizon.md
  secoes:
  - introduction
  - installation
  - balancing-strategies
  - upgrading-horizon
  - running-horizon
  - tags
  tokens_estimados: 7159
- id: http-client
  resumo: '[!WARNING] If all of the requests fail because of a connection issue, a
    `Illuminate\Http\Client\ConnectionException` will still be thrown even when the
    `throw` argument is set to `false`.'
  gatilhos:
  - client
  - frameworks
  - http
  - laravel
  arquivo: ./http-client.md
  secoes:
  - introduction
  - making-requests
  - concurrent-requests
  - macros
  - testing
  - events
  tokens_estimados: 8841
- id: http-tests
  resumo: '[!NOTE] For convenience, the CSRF middleware is automatically disabled
    when running tests.'
  gatilhos:
  - frameworks
  - http
  - laravel
  - tests
  arquivo: ./http-tests.md
  secoes:
  - introduction
  - making-requests
  - testing-json-apis
  - testing-file-uploads
  - testing-views
  - caching-routes
  tokens_estimados: 14710
- id: installation
  resumo: '[!NOTE] For a fully-featured, graphical PHP installation and management
    experience, check out [Laravel Herd](#installation-using-herd).'
  gatilhos:
  - frameworks
  - installation
  - laravel
  arquivo: ./installation.md
  secoes:
  - meet-laravel
  - creating-a-laravel-application
  - initial-configuration
  - installation-using-herd
  - ide-support
  - laravel-and-ai
  tokens_estimados: 4650
- id: laravel-12-x
  resumo: '**Arquivo Original:** `laravel-12.x.pdf` **Data Conversão:** 1766671573.2565825'
  gatilhos:
  - 12.x
  - frameworks
  - laravel
  arquivo: ./laravel-12.x.md
  secoes:
  - página-1
  - página-2
  - página-3
  - página-4
  - página-5
  - página-6
  tokens_estimados: 676167
- id: lifecycle
  resumo: Guia tecnico e referencias sobre Request Lifecycle.
  gatilhos:
  - frameworks
  - laravel
  - lifecycle
  - request
  arquivo: ./lifecycle.md
  secoes:
  - introduction
  - lifecycle-overview
  - focus-on-service-providers
  tokens_estimados: 1852
- id: localization
  resumo: '[!NOTE] By default, the Laravel application skeleton does not include the
    `lang` directory. If you would like to customize Laravel''s language files, you
    may publish them via the `lang:publish` Artisan command.'
  gatilhos:
  - frameworks
  - laravel
  - localization
  arquivo: ./localization.md
  secoes:
  - introduction
  - defining-translation-strings
  - retrieving-translation-strings
  - overriding-package-language-files
  tokens_estimados: 3156
- id: logging
  resumo: '[!NOTE] Check out the documentation on [advanced channel customization](#monolog-channel-customization)
    to learn more about the `monolog` and `custom` drivers.'
  gatilhos:
  - frameworks
  - laravel
  - logging
  arquivo: ./logging.md
  secoes:
  - introduction
  - configuration
  - building-log-stacks
  - writing-log-messages
  - monolog-channel-customization
  - tailing-log-messages-using-pail
  tokens_estimados: 5920
- id: mail
  resumo: '[!NOTE] You may wish to create a `resources/views/mail` directory to house
    all of your email templates; however, you are free to place them wherever you
    wish within your `resources/views` directory.'
  gatilhos:
  - frameworks
  - laravel
  - mail
  arquivo: ./mail.md
  secoes:
  - introduction
  - generating-mailables
  - writing-mailables
  - markdown-mailables
  - sending-mail
  - rendering-mailables
  tokens_estimados: 14434
- id: mcp
  resumo: '[!NOTE] The description is a critical part of the tool''s metadata, as
    it helps AI models understand when and how to use the tool effectively.'
  gatilhos:
  - frameworks
  - laravel
  - mcp
  arquivo: ./mcp.md
  secoes:
  - introduction
  - installation
  - creating-servers
  - tools
  - prompts
  - resources
  tokens_estimados: 21140
- id: middleware
  resumo: '[!NOTE] All middleware are resolved via the [service container](/docs/{{version}}/container),
    so you may type-hint any dependencies you need within a middleware''s constructor.'
  gatilhos:
  - frameworks
  - laravel
  - middleware
  arquivo: ./middleware.md
  secoes:
  - introduction
  - defining-middleware
  - registering-middleware
  - middleware-parameters
  - terminable-middleware
  tokens_estimados: 4919
- id: migrations
  resumo: '[!NOTE] Migration stubs may be customized using [stub publishing](/docs/{{version}}/artisan#stub-customization).'
  gatilhos:
  - database
  - frameworks
  - laravel
  - migrations
  arquivo: ./migrations.md
  secoes:
  - introduction
  - generating-migrations
  - migration-structure
  - running-migrations
  - tables
  - columns
  tokens_estimados: 13899
- id: mix
  resumo: '[!WARNING] Laravel Mix is a legacy package that is no longer actively maintained.
    [Vite](/docs/{{version}}/vite) may be used as a modern alternative.'
  gatilhos:
  - frameworks
  - laravel
  - mix
  arquivo: ./mix.md
  secoes:
  - introduction
  tokens_estimados: 369
- id: mocking
  resumo: '[!WARNING] You should not mock the `Request` facade. Instead, pass the
    input you desire into the [HTTP testing methods](/docs/{{version}}/http-tests)
    such as `get` and `post` when running your test. Likewise, instead of mocking
    the `Config` facade...'
  gatilhos:
  - frameworks
  - laravel
  - mocking
  arquivo: ./mocking.md
  secoes:
  - introduction
  - mocking-objects
  - mocking-facades
  - interacting-with-time
  tokens_estimados: 2316
- id: mongodb
  resumo: '[!NOTE] This installation of the package will fail if the `mongodb` PHP
    extension is not installed. The PHP configuration can differ between the CLI and
    the web server, so ensure the extension is enabled in both configurations.'
  gatilhos:
  - frameworks
  - laravel
  - mongodb
  arquivo: ./mongodb.md
  secoes:
  - introduction
  - installation
  - configuration
  - features
  tokens_estimados: 1470
- id: notifications
  resumo: '[!NOTE] Remember, you may use the `Notifiable` trait on any of your models.
    You are not limited to only including it on your `User` model.'
  gatilhos:
  - frameworks
  - laravel
  - notifications
  arquivo: ./notifications.md
  secoes:
  - introduction
  - generating-notifications
  - sending-notifications
  - mail-notifications
  - markdown-mail-notifications
  - database-notifications
  tokens_estimados: 18604
- id: octane
  resumo: '[!WARNING] Before serving an Octane application via Sail, ensure you have
    the latest version of Laravel Sail and execute `./vendor/bin/sail build --no-cache`
    within your application''s root directory.'
  gatilhos:
  - frameworks
  - laravel
  - octane
  arquivo: ./octane.md
  secoes:
  - introduction
  - installation
  - server-prerequisites
  - serving-your-application
  - dependency-injection-and-octane
  - concurrent-tasks
  tokens_estimados: 7371
- id: packages
  resumo: '[!WARNING] You should not define closures in your configuration files.
    They cannot be serialized correctly when users execute the `config:cache` Artisan
    command.'
  gatilhos:
  - development
  - frameworks
  - laravel
  - package
  - packages
  arquivo: ./packages.md
  secoes:
  - introduction
  - package-discovery
  - service-providers
  - resources
  - commands
  - public-assets
  tokens_estimados: 4615
- id: pagination
  resumo: '[!WARNING] Your query must contain an "order by" clause in order to take
    advantage of cursor pagination. In addition, the columns that the query are ordered
    by must belong to the table you are paginating.'
  gatilhos:
  - database
  - frameworks
  - laravel
  - pagination
  arquivo: ./pagination.md
  secoes:
  - introduction
  - basic-usage
  - displaying-pagination-results
  - customizing-the-pagination-view
  - paginator--lengthawarepaginator-instance-methods
  - cursor-paginator-instance-methods
  tokens_estimados: 5605
- id: passport
  resumo: '[!NOTE] This documentation assumes you are already familiar with OAuth2.
    If you do not know anything about OAuth2, consider familiarizing yourself with
    the general [terminology](https://oauth2.thephpleague.com/terminology/) and features
    of OAuth2 ...'
  gatilhos:
  - frameworks
  - laravel
  - passport
  arquivo: ./passport.md
  secoes:
  - introduction
  - installation
  - configuration
  - authorization-code-grant
  - authorization-code-grant-with-pkce
  - device-authorization-grant
  tokens_estimados: 14665
- id: passwords
  resumo: '[!NOTE] Want to get started fast? Install a Laravel [application starter
    kit](/docs/{{version}}/starter-kits) in a fresh Laravel application. Laravel''s
    starter kits will take care of scaffolding your entire authentication system,
    including resetti...'
  gatilhos:
  - frameworks
  - laravel
  - passwords
  - resetting
  arquivo: ./passwords.md
  secoes:
  - introduction
  - routing
  - deleting-expired-tokens
  - customization
  tokens_estimados: 3722
- id: pennant
  resumo: '[!NOTE] Feature classes are resolved via the [container](/docs/{{version}}/container),
    so you may inject dependencies into the feature class''s constructor when needed.'
  gatilhos:
  - frameworks
  - laravel
  - pennant
  arquivo: ./pennant.md
  secoes:
  - introduction
  - installation
  - configuration
  - defining-features
  - checking-features
  - scope
  tokens_estimados: 10200
- id: pint
  resumo: Guia tecnico e referencias sobre Laravel Pint.
  gatilhos:
  - frameworks
  - laravel
  - pint
  arquivo: ./pint.md
  secoes:
  - introduction
  - installation
  - running-pint
  - configuring-pint
  - continuous-integration
  tokens_estimados: 1748
- id: precognition
  resumo: '[!NOTE] As of Inertia 2.3, Precognition support is built-in. Please consult
    the [Inertia Forms documentation](https://inertiajs.com/docs/v2/the-basics/forms)
    for more information. Earlier Inertia versions require Precognition 0.x.'
  gatilhos:
  - frameworks
  - laravel
  - precognition
  arquivo: ./precognition.md
  secoes:
  - introduction
  - live-validation
  - customizing-validation-rules
  - handling-file-uploads
  - managing-side-effects
  - testing
  tokens_estimados: 5960
- id: processes
  resumo: '[!WARNING] TTY mode is not supported on Windows.'
  gatilhos:
  - frameworks
  - laravel
  - processes
  arquivo: ./processes.md
  secoes:
  - introduction
  - invoking-processes
  - asynchronous-processes
  - concurrent-processes
  - testing
  tokens_estimados: 5880
- id: prompts
  resumo: '[!NOTE] Laravel Prompts supports macOS, Linux, and Windows with WSL. For
    more information, please see our documentation on [unsupported environments &
    fallbacks](#fallbacks).'
  gatilhos:
  - frameworks
  - laravel
  - prompts
  arquivo: ./prompts.md
  secoes:
  - introduction
  - installation
  - available-prompts
  - transforming-input-before-validation
  - forms
  - informational-messages
  tokens_estimados: 8293
- id: providers
  resumo: '[!NOTE] If you would like to learn more about how Laravel handles requests
    and works internally, check out our documentation on the Laravel [request lifecycle](/docs/{{version}}/lifecycle).'
  gatilhos:
  - frameworks
  - laravel
  - providers
  - service
  arquivo: ./providers.md
  secoes:
  - introduction
  - writing-service-providers
  - registering-providers
  - deferred-providers
  tokens_estimados: 2121
- id: pulse
  resumo: '[!WARNING] Pulse''s first-party storage implementation currently requires
    a MySQL, MariaDB, or PostgreSQL database. If you are using a different database
    engine, you will need a separate MySQL, MariaDB, or PostgreSQL database for your
    Pulse data.'
  gatilhos:
  - frameworks
  - laravel
  - pulse
  arquivo: ./pulse.md
  secoes:
  - introduction
  - installation
  - dashboard
  - capturing-entries
  - performance
  - custom-cards
  tokens_estimados: 8352
- id: queries
  resumo: '[!WARNING] PDO does not support binding column names. Therefore, you should
    never allow user input to dictate the column names referenced by your queries,
    including "order by" columns.'
  gatilhos:
  - builder
  - database
  - frameworks
  - laravel
  - queries
  - query
  arquivo: ./queries.md
  secoes:
  - introduction
  - running-database-queries
  - select-statements
  - raw-expressions
  - joins
  - unions
  tokens_estimados: 13979
- id: queues
  resumo: '[!NOTE] Laravel Horizon is a beautiful dashboard and configuration system
    for your Redis powered queues. Check out the full [Horizon documentation](/docs/{{version}}/horizon)
    for more information.'
  gatilhos:
  - frameworks
  - laravel
  - queues
  arquivo: ./queues.md
  secoes:
  - introduction
  - creating-jobs
  - job-middleware
  - dispatching-jobs
  - job-batching
  - queueing-closures
  tokens_estimados: 30173
- id: rate-limiting
  resumo: '[!NOTE] If you are interested in rate limiting incoming HTTP requests,
    please consult the [rate limiter middleware documentation](/docs/{{version}}/routing#rate-limiting).'
  gatilhos:
  - frameworks
  - laravel
  - limiting
  - rate
  arquivo: ./rate-limiting.md
  secoes:
  - introduction
  - basic-usage
  tokens_estimados: 1195
- id: redirects
  resumo: Guia tecnico e referencias sobre HTTP Redirects.
  gatilhos:
  - frameworks
  - http
  - laravel
  - redirects
  arquivo: ./redirects.md
  secoes:
  - creating-redirects
  - redirecting-to-named-routes
  - redirecting-to-controller-actions
  - redirecting-with-flashed-session-data
  tokens_estimados: 1119
- id: redis
  resumo: '[!WARNING] When defining a Redis transaction, you may not retrieve any
    values from the Redis connection. Remember, your transaction is executed as a
    single, atomic operation and that operation is not executed until your entire
    closure has finished...'
  gatilhos:
  - frameworks
  - laravel
  - redis
  arquivo: ./redis.md
  secoes:
  - introduction
  - configuration
  - interacting-with-redis
  - pub--sub
  tokens_estimados: 4318
- id: releases
  resumo: Guia tecnico e referencias sobre Release Notes.
  gatilhos:
  - frameworks
  - laravel
  - notes
  - release
  - releases
  arquivo: ./releases.md
  secoes:
  - versioning-scheme
  - support-policy
  - laravel-12
  tokens_estimados: 1132
- id: requests
  resumo: '[!NOTE] If you return a PSR-7 response instance from a route or controller,
    it will automatically be converted back to a Laravel response instance and be
    displayed by the framework.'
  gatilhos:
  - frameworks
  - http
  - laravel
  - requests
  arquivo: ./requests.md
  secoes:
  - introduction
  - interacting-with-the-request
  - input
  - input-trimming-and-normalization
  - files
  - configuring-trusted-proxies
  tokens_estimados: 7919
- id: responses
  resumo: '[!NOTE] Did you know you can also return [Eloquent collections](/docs/{{version}}/eloquent-collections)
    from your routes or controllers? They will automatically be converted to JSON.
    Give it a shot!'
  gatilhos:
  - frameworks
  - http
  - laravel
  - responses
  arquivo: ./responses.md
  secoes:
  - creating-responses
  - redirects
  - other-response-types
  - streamed-responses
  - response-macros
  tokens_estimados: 7422
- id: reverb
  resumo: '[!NOTE] If your site is managed by [Laravel Forge](https://forge.laravel.com),
    you may automatically optimize your server for Reverb directly from the "Application"
    panel. By enabling the Reverb integration, Forge will ensure your server is produc...'
  gatilhos:
  - frameworks
  - laravel
  - reverb
  arquivo: ./reverb.md
  secoes:
  - introduction
  - installation
  - configuration
  - running-the-server
  - monitoring
  - running-reverb-in-production
  tokens_estimados: 3993
- id: routing
  resumo: '[!NOTE] When defining multiple routes that share the same URI, routes using
    the `get`, `post`, `put`, `patch`, `delete`, and `options` methods should be defined
    before routes using the `any`, `match`, and `redirect` methods. This ensures the
    incom...'
  gatilhos:
  - frameworks
  - laravel
  - routing
  arquivo: ./routing.md
  secoes:
  - basic-routing
  - route-parameters
  - named-routes
  - route-groups
  - route-model-binding
  - fallback-routes
  tokens_estimados: 10128
- id: sail
  resumo: '[!WARNING] If you are using Docker Desktop for Linux, you should use the
    `default` Docker context by executing the following command: `docker context use
    default`. In addition, if you encounter file permission errors within containers,
    you may nee...'
  gatilhos:
  - frameworks
  - laravel
  - sail
  arquivo: ./sail.md
  secoes:
  - introduction
  - installation-and-setup
  - starting-and-stopping-sail
  - executing-commands
  - interacting-with-databases
  - file-storage
  tokens_estimados: 6349
- id: sanctum
  resumo: '[!NOTE] It is perfectly fine to use Sanctum only for API token authentication
    or only for SPA authentication. Just because you use Sanctum does not mean you
    are required to use both features it offers.'
  gatilhos:
  - frameworks
  - laravel
  - sanctum
  arquivo: ./sanctum.md
  secoes:
  - introduction
  - installation
  - configuration
  - api-token-authentication
  - spa-authentication
  - mobile-application-authentication
  tokens_estimados: 6450
- id: scheduling
  resumo: '[!WARNING] Remember that some timezones utilize daylight savings time.
    When daylight saving time changes occur, your scheduled task may run twice or
    even not run at all. For this reason, we recommend avoiding timezone scheduling
    when possible.'
  gatilhos:
  - frameworks
  - laravel
  - scheduling
  - task
  arquivo: ./scheduling.md
  secoes:
  - introduction
  - defining-schedules
  - running-the-scheduler
  - task-output
  - task-hooks
  - events
  tokens_estimados: 7113
- id: scout
  resumo: '[!WARNING] When upgrading Scout on an application that utilizes Meilisearch,
    you should always [review any additional breaking changes](https://github.com/meilisearch/Meilisearch/releases)
    to the Meilisearch service itself.'
  gatilhos:
  - frameworks
  - laravel
  - scout
  arquivo: ./scout.md
  secoes:
  - introduction
  - installation
  - driver-prerequisites
  - configuration
  - database--collection-engines
  - indexing
  tokens_estimados: 9667
- id: seeding
  resumo: '[!NOTE] [Mass assignment protection](/docs/{{version}}/eloquent#mass-assignment)
    is automatically disabled during database seeding.'
  gatilhos:
  - database
  - frameworks
  - laravel
  - seeding
  arquivo: ./seeding.md
  secoes:
  - introduction
  - writing-seeders
  - running-seeders
  tokens_estimados: 1388
- id: session
  resumo: '[!NOTE] The array driver is primarily used during [testing](/docs/{{version}}/testing)
    and prevents the data stored in the session from being persisted.'
  gatilhos:
  - frameworks
  - http
  - laravel
  - session
  arquivo: ./session.md
  secoes:
  - introduction
  - interacting-with-the-session
  - session-cache
  - session-blocking
  - adding-custom-session-drivers
  tokens_estimados: 4529
- id: socialite
  resumo: '[!NOTE] Adapters for other platforms are available via the community driven
    [Socialite Providers](https://socialiteproviders.com/) website.'
  gatilhos:
  - frameworks
  - laravel
  - socialite
  arquivo: ./socialite.md
  secoes:
  - introduction
  - installation
  - upgrading-socialite
  - configuration
  - authentication
  - retrieving-user-details
  tokens_estimados: 2819
- id: starter-kits
  resumo: '[!NOTE] Email verification is not required when using the [WorkOS](#workos)
    variant of the starter kits.'
  gatilhos:
  - frameworks
  - kits
  - laravel
  - starter
  arquivo: ./starter-kits.md
  secoes:
  - introduction
  - creating-an-application-using-a-starter-kit
  - available-starter-kits
  - starter-kit-customization
  - authentication
  - workos-authkit-authentication
  tokens_estimados: 5899
- id: strings
  resumo: Guia tecnico e referencias sobre Strings.
  gatilhos:
  - frameworks
  - laravel
  - strings
  arquivo: ./strings.md
  secoes:
  - introduction
  - available-methods
  - strings
  - fluent-strings
  tokens_estimados: 25238
- id: structure
  resumo: '[!NOTE] Many of the classes in the `app` directory can be generated by
    Artisan via commands. To review the available commands, run the `php artisan list
    make` command in your terminal.'
  gatilhos:
  - directory
  - frameworks
  - laravel
  - structure
  arquivo: ./structure.md
  secoes:
  - introduction
  - the-root-directory
  - the-app-directory
  tokens_estimados: 3350
- id: telescope
  resumo: '[!WARNING] You should ensure you change your `APP_ENV` environment variable
    to `production` in your production environment. Otherwise, your Telescope installation
    will be publicly available.'
  gatilhos:
  - frameworks
  - laravel
  - telescope
  arquivo: ./telescope.md
  secoes:
  - introduction
  - installation
  - upgrading-telescope
  - filtering
  - tagging
  - available-watchers
  tokens_estimados: 4324
- id: testing
  resumo: '[!NOTE] Test stubs may be customized using [stub publishing](/docs/{{version}}/artisan#stub-customization).'
  gatilhos:
  - frameworks
  - getting
  - laravel
  - started
  - testing
  arquivo: ./testing.md
  secoes:
  - introduction
  - environment
  - creating-tests
  - running-tests
  - configuration-caching
  tokens_estimados: 2640
- id: upgrade
  resumo: '[!NOTE] We attempt to document every possible breaking change. Since some
    of these breaking changes are in obscure parts of the framework only a portion
    of these changes may actually affect your application. Want to save time? You
    can use [Laravel...'
  gatilhos:
  - frameworks
  - guide
  - laravel
  - upgrade
  arquivo: ./upgrade.md
  secoes:
  - high-impact-changes
  - medium-impact-changes
  - low-impact-changes
  - upgrading-to-120-from-11x
  tokens_estimados: 2341
- id: urls
  resumo: Guia tecnico e referencias sobre URL Generation.
  gatilhos:
  - frameworks
  - generation
  - laravel
  - url
  - urls
  arquivo: ./urls.md
  secoes:
  - introduction
  - the-basics
  - urls-for-named-routes
  - urls-for-controller-actions
  - fluent-uri-objects
  - default-values
  tokens_estimados: 3259
- id: valet
  resumo: '[!NOTE] Looking for an even easier way to develop Laravel applications
    on macOS or Windows? Check out [Laravel Herd](https://herd.laravel.com). Herd
    includes everything you need to get started with Laravel development, including
    Valet, PHP, and Co...'
  gatilhos:
  - frameworks
  - laravel
  - valet
  arquivo: ./valet.md
  secoes:
  - introduction
  - installation
  - serving-sites
  - sharing-sites
  - site-specific-environment-variables
  - proxying-services
  tokens_estimados: 6272
- id: validation
  resumo: '[!WARNING] By default, the Laravel application skeleton does not include
    the `lang` directory. If you would like to customize Laravel''s language files,
    you may publish them via the `lang:publish` Artisan command.'
  gatilhos:
  - frameworks
  - laravel
  - validation
  arquivo: ./validation.md
  secoes:
  - introduction
  - validation-quickstart
  - form-request-validation
  - manually-creating-validators
  - working-with-validated-input
  - working-with-error-messages
  tokens_estimados: 27008
- id: verification
  resumo: '[!NOTE] Want to get started fast? Install one of the [Laravel application
    starter kits](/docs/{{version}}/starter-kits) in a fresh Laravel application.
    The starter kits will take care of scaffolding your entire authentication system,
    including ema...'
  gatilhos:
  - email
  - frameworks
  - laravel
  - verification
  arquivo: ./verification.md
  secoes:
  - introduction
  - routing
  - customization
  - events
  tokens_estimados: 2403
- id: views
  resumo: '[!NOTE] Looking for more information on how to write Blade templates? Check
    out the full [Blade documentation](/docs/{{version}}/blade) to get started.'
  gatilhos:
  - frameworks
  - laravel
  - views
  arquivo: ./views.md
  secoes:
  - introduction
  - creating-and-rendering-views
  - passing-data-to-views
  - view-composers
  - optimizing-views
  tokens_estimados: 2790
- id: vite
  resumo: '[!NOTE] The following documentation discusses how to manually install and
    configure the Laravel Vite plugin. However, Laravel''s [starter kits](/docs/{{version}}/starter-kits)
    already include all of this scaffolding and are the fastest way to get s...'
  gatilhos:
  - asset
  - bundling
  - frameworks
  - laravel
  - vite
  arquivo: ./vite.md
  secoes:
  - introduction
  - installation--setup
  - running-vite
  - working-with-javascript
  - working-with-stylesheets
  - working-with-blade-and-routes
  tokens_estimados: 9174
---

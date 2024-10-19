from django.contrib import admin
from .models import Movie, Show, LiveNews, Plan, Subscription, Payment, ShortVideo, Ad, UserProfile

# Registering the Movie model
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'release_date', 'status', 'is_trending')
    search_fields = ('title', 'genre', 'language')
    list_filter = ('genre', 'status', 'is_trending')
    ordering = ('-release_date',)

# Registering the Show model
@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'release_date', 'status', 'is_trending')
    search_fields = ('title', 'genre', 'language')
    list_filter = ('genre', 'status', 'is_trending')
    ordering = ('-release_date',)

# Registering the LiveNews model
@admin.register(LiveNews)
class LiveNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_url', 'is_active')
    search_fields = ('title', 'youtube_url')
    list_filter = ('is_active',)

# Registering the Plan model
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'price', 'duration')
    search_fields = ('plan_name',)
    ordering = ('-price',)

# Registering the Subscription model
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'is_active')
    search_fields = ('user__username', 'plan__plan_name')
    list_filter = ('is_active',)

# Registering the Payment model
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'amount', 'payment_method', 'payment_status', 'payment_date')
    search_fields = ('subscription__user__username',)
    list_filter = ('payment_method', 'payment_status')

# Registering the ShortVideo model
@admin.register(ShortVideo)
class ShortVideoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'upload_date')
    search_fields = ('title', 'user__username')

# Registering the Ad model
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
    search_fields = ('title',)
    list_filter = ('status',)

# Registering the UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'is_verified')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('is_verified',)
